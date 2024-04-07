from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/verify": {"origins": "*"}}) # 配置CORS，允许所有来源
@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    if not data:
        return 'Bad Request', 400
    name = data.get('name')
    email = data.get('email')
    # 对数据进行验证处理
    return jsonify({'message': '数据已接收', 'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
