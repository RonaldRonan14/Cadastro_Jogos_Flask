from flask import Blueprint, render_template, request, redirect
from Model.models import db, Jogos
from datetime import datetime

routes = Blueprint("routes", __name__)

#View
@routes.route("/")
def index():
    lista_jogos = Jogos.query.all()
    return render_template('index.html', jogos=lista_jogos)

#View
@routes.route("/create")
def create():
    return render_template('create.html')

#Action
@routes.route("/create", methods=['POST'])
def create_post():
    nome_jogo = request.form['nome_jogo']
    data_criacao_jogo_str = request.form['data_criacao_jogo']
    data_criacao_jogo = datetime.strptime(data_criacao_jogo_str, '%Y-%m-%d')
    classificacao_jogo = request.form['classificacao_jogo']

    novo = Jogos(
        nome_jogo = nome_jogo,
        data_criacao_jogo = data_criacao_jogo,
        classificacao_jogo = classificacao_jogo
    )
    db.session.add(novo)
    db.session.commit()

    return redirect("/")

#View
@routes.route("/edit/<int:id>")
def edit(id):
    jogo = Jogos.query.get(id)

    if jogo:
        return render_template('edit.html', jogo = jogo)
    else:
        return redirect("/")

#Action
@routes.route("/edit/<int:id>", methods=['POST'])
def edit_post(id):
    jogo = Jogos.query.get(id)

    nome_jogo = request.form['nome_jogo']
    data_criacao_jogo_str = request.form['data_criacao_jogo']
    data_criacao_jogo = datetime.strptime(data_criacao_jogo_str, '%Y-%m-%d')
    classificacao_jogo = request.form['classificacao_jogo']

    jogo.nome_jogo = nome_jogo
    jogo.data_criacao_jogo = data_criacao_jogo
    jogo.classificacao_jogo = classificacao_jogo

    db.session.commit()
    
    return redirect("/")

@routes.route("/delete/<int:id>")
def delete(id):
    jogo = Jogos.query.get(id)

    if jogo:
        nome_jogo = jogo.nome_jogo

        return render_template('delete.html', nome_jogo = nome_jogo)
    else:
        return redirect("/")

@routes.route("/delete/<int:id>", methods=['POST'])
def delete_post(id):
    jogo = Jogos.query.get(id)

    if jogo:
        db.session.delete(jogo)
        db.session.commit()

    return redirect("/")