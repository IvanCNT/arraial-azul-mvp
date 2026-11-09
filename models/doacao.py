from app import db

class Doacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    tipo_doacao = db.Column(db.String(80))
    descricao = db.Column(db.String(200))
    quantidade = db.Column(db.Integer)

    data_doacao = db.Column(db.Date)

    voluntario_id = db.Column(
        db.Integer,
        db.ForeignKey('voluntario.id')
    )
