from Model.models import db

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base_jogos.db'
    db.init_app(app)

    with app.app_context():
        db.create_all()