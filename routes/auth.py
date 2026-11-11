from flask import Blueprint, request
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

auth = Blueprint("auth", __name__)

def criar_usuario(nome, email, senha):

    senha_hash = generate_password_hash(
        senha,
        method="pbkdf2:sha256"
    )

    novo_usuario = Usuario(
        nome=nome,
        email=email,
        senha_hash=senha_hash
    )

    return novo_usuario


def validar_login(usuario, senha_digitada):

    return check_password_hash(
        usuario.senha_hash,
        senha_digitada
    )
