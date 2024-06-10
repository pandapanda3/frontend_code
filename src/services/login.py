from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# 模拟的用户数据
users = {
    "admin@kcl.ac.uk": "admin"
}

@app.route('/api/login', methods=['POST'])
def login():
    # 获取请求中的JSON数据
    data = request.get_json()

    # 获取用户名和密码
    username = data.get('username')
    password = data.get('password')

    # 检查用户名和密码是否正确
    if username in users and users[username] == password:
        # 返回成功响应
        return jsonify({"message": "Login successful", "status": "success"}), 200
    else:
        # 返回失败响应
        return jsonify({"message": "Invalid username or password", "status": "fail"}), 401

if __name__ == '__main__':
    app.run(debug=True)

