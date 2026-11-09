from app import db

class Voluntario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(14), unique=True)
    telefone = db.Column(db.String(20))
    funcao = db.Column(db.String(60))
    disponibilidade = db.Column(db.String(120))
