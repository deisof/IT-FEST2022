from flask import Flask
from flask import render_template, make_response, jsonify
from flask_login import LoginManager
from flask_restful import Api
from data import card_api, db_session
from data import user_api
from data.users import User
from waitress import serve
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
api = Api(app)
MAX_CONTENT_LENGTH = 1024 * 1024


def main():
    db_session.global_init("db/it-fest.db")

    @login_manager.user_loader
    def load_user(user_id):
        session = db_session.create_session()
        return session.query(User).get(user_id)

    app.register_blueprint(card_api.blueprint)
    app.register_blueprint(user_api.blueprint)

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html')

    serve(app, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
