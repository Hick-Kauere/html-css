
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de um banco de dados de usuários
USERS = {
    "hick": "123",
    "user": "password"
}

@app.route('/cad', methods=['POST'])
def login():
    data = request.form
    username = data.get('usuario')
    password = data.get('senha')

    if not username or not password:
        return jsonify({"success": False, "message": "Usuário e senha são obrigatórios."}), 400

    if username in USERS and USERS[username] == password:
        return jsonify({"success": True, "message": "Login bem-sucedido!"}), 200
    else:
        return jsonify({"success": False, "message": "Usuário ou senha inválidos."}), 401

if __name__ == '__main__':
    app.run(debug=True, port=5000)

