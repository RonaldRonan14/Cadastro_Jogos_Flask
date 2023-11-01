from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Jogos(db.Model):
    id_jogo = db.Column(db.Integer, primary_key=True)
    nome_jogo = db.Column(db.String(80), nullable=False)
    data_criacao_jogo = db.Column(db.Date, nullable=False)
    classificacao_jogo = db.Column(db.Integer, nullable=True)