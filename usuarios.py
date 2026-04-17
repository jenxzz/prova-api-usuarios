from flask import Flask, jsonify
import os

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Maria"},
    {"id": 2, "nome": "João"},
    {"id": 3, "nome": "Ana"}
]

@app.route("/usuarios", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Usuários - Acesse /"})

@app.route("/", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)