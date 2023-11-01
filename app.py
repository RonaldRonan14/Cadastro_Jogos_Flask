from flask import Flask
from routes import routes
from Model.context import init_db

app = Flask(__name__)

# Rotas
app.register_blueprint(routes)

# Config Banco
init_db(app)

if __name__ == "__main__":
    app.run(debug=True)