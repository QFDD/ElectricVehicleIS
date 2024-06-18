from flaskr.auth import login_required
from flaskr.db import get_db
from flask import (
    Blueprint, jsonify, g, redirect, render_template, request, session, url_for, Flask, make_response
)
from flaskr import db

bp = Blueprint('chat', __name__, url_prefix='/chat')

@bp.route('/<int:conversation_id>/messages', methods=['GET'])
def get_messages(conversation_id):
    conn = db.get_db()
    cursor = conn.cursor()
    messages = cursor.execute('SELECT message_id, conversation_id, sender_id, message_text, sent_at FROM messages WHERE conversation_id = ?',
                            (conversation_id,)).fetchall()
    result = []
    for message in messages:
        result.append({
            "message_id": message[0],
            "conversation_id": message[1],
            "sender_id": message[2],
            "message_text": message[3],
            "sent_at": message[4]
        })
    return jsonify(result)

@bp.route('/send_messages', methods=['POST'])
def send_message():
    new_message = request.get_json()
    conversation_id = new_message['conversation_id']
    sender_id = new_message['sender_id']
    message_text = new_message['message_text']

    conn = db.get_db()
    cursor = conn.cursor()
     # 检查会话是否存在，如果不存在则创建会话
    conversation = cursor.execute('SELECT * FROM conversations WHERE conversation_id = ?',
                                  (conversation_id,)).fetchone()
    if conversation is None:
        cursor.execute('INSERT INTO conversations (conversation_name) VALUES (?)',
                       ('New Conversation',))
        conversation_id = cursor.lastrowid

        # 插入会话参与者
        cursor.execute('INSERT INTO conversation_participants (conversation_id, user_id) VALUES (?, ?)',
                       (conversation_id, sender_id))
        # 假设接收者的用户ID为2，这里需要根据实际情况调整
        receiver_id = 2
        cursor.execute('INSERT INTO conversation_participants (conversation_id, user_id) VALUES (?, ?)',
                       (conversation_id, receiver_id))
    cursor.execute('INSERT INTO messages (conversation_id, sender_id, message_text) VALUES (?, ?, ?)',
                 (conversation_id, sender_id, message_text))
    conn.commit()
    message_id = cursor.execute('SELECT last_insert_rowid()').fetchone()[0]
    conn.close()

    response_message = {
        'message_id': message_id,
        'conversation_id': conversation_id,
        'sender_id': sender_id,
        'message_text': message_text,
        'sent_at': 'now'  # 假设是当前时间，可以根据需要调整
    }
    return jsonify(response_message), 201

@bp.route('/check_conversation', methods=['GET'])
def check_conversation():
    user1 = request.args.get('user1')
    user2 = request.args.get('user2')

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT cp1.conversation_id
    FROM conversation_participants cp1
    JOIN conversation_participants cp2
    ON cp1.conversation_id = cp2.conversation_id
    WHERE cp1.user_id = ? AND cp2.user_id = ?
    AND cp1.user_id IS NOT NULL AND cp2.user_id IS NOT NULL
    ''', (user1, user2))

    conversation = cursor.fetchone()

    if conversation:
        conversation_id = conversation[0]
        print("conversation"+str(conversation_id)+ "exist")
        conn = db.get_db()
        cursor = conn.cursor()
        messages = cursor.execute('SELECT message_id, conversation_id, sender_id, message_text, sent_at FROM messages WHERE conversation_id = ?',
                                (conversation_id,)).fetchall()
        results = []
        for message in messages:
            results.append({
                "message_id": message[0],
                "conversation_id": message[1],
                "sender_id": message[2],
                "message_text": message[3],
                "sent_at": message[4]
            })
        return jsonify({
            'conversation_id': conversation_id,
            'messages': results
        })

    else:
        print("not exist")
        cursor.execute('''
        INSERT INTO conversations (conversation_name) VALUES (?)
        ''', (f"Conversation between {user1} and {user2}",))
        conversation_id = cursor.lastrowid

        cursor.execute('''
        INSERT INTO conversation_participants (conversation_id, user_id) VALUES (?, ?)
        ''', (conversation_id, user1))
        cursor.execute('''
        INSERT INTO conversation_participants (conversation_id, user_id) VALUES (?, ?)
        ''', (conversation_id, user2))

        conn.commit()
        conn.close()

        return jsonify({
            'conversation_id': conversation_id,
            'messages': []
        })

    