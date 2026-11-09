from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'trocar-em-producao'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arraial.db'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from routes.auth import auth
from routes.voluntarios import voluntarios
from routes.doacoes import doacoes

app.register_blueprint(auth)
app.register_blueprint(voluntarios)
app.register_blueprint(doacoes)

if __name__ == "__main__":
    app.run(debug=True)
