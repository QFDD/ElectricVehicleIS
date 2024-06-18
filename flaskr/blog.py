from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import BadRequest
from flaskr.auth import login_required
from flaskr.db import get_db
from datetime import datetime
bp = Blueprint('blog', __name__)

@bp.route('/blog/posts', methods=['GET'])
def get_posts():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit

    conn = get_db()
    cursor = conn.cursor()
    posts = cursor.execute('SELECT * FROM posts LIMIT ? OFFSET ?', (limit, offset)).fetchall()
    total_posts = cursor.execute('SELECT COUNT(*) FROM posts').fetchone()[0]
    conn.close()

    has_more_posts = (page * limit) < total_posts

    posts_data = []
    for post in posts:
        posts_data.append({
            'id': post[0],
            'user_id': post[1],
            'title': post[2],
            'content': post[3],
            'created_at': post[4]
        })
        
    response = {
        'posts': posts_data,
        'hasMorePosts': has_more_posts
    }

    return jsonify(response)

@bp.route('/blog/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    title = new_post['title']
    content = new_post['content']
    user_id = new_post['user_id']
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = get_db()
    conn.execute('INSERT INTO posts (user_id, title, content, created_at) VALUES (?, ?, ?, ?)',
                 (user_id, title, content, created_at))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Post created successfully'}), 201

@bp.route('/blog/posts/<int:id>', methods=['GET'])
def get_post(id):
    conn = get_db()
    post = conn.execute('SELECT id,user_id,title,content,created_at FROM posts WHERE id = ?', (id,)).fetchone()
    conn.close()

    if post is None:
        return jsonify({'message': 'Post not found'}), 404

    post_data = {
        'id': post[0],
        'user_id': post[1],
        'title': post[2],
        'content': post[3],
        'created_at': post[4]
    }

    return jsonify({'post': post_data})

@bp.route('/blog/posts/<int:post_id>/comments', methods=['GET'])
def get_comments(post_id):
    conn = get_db()
    comments = conn.execute('SELECT id,post_id,user_id,content,created_at FROM comments WHERE post_id = ?', (post_id,)).fetchall()
    conn.close()

    comments_data = []
    for comment in comments:
        comments_data.append({
            'id': comment[0],
            'post_id': comment[1],
            'user_id': comment[2],
            'content': comment[3],
            'created_at': comment[4]
        })

    return jsonify({'comments': comments_data})