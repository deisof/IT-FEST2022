import flask
from flask import render_template, request
from flask_login import login_user, login_required, logout_user
from werkzeug.utils import redirect
from data import db_session
from data.users import User

blueprint = flask.Blueprint('user_api', __name__, template_folder='templates')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session = db_session.create_session()
        user = session.query(User).filter(
            User.email == request.form['email']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect("/profile")
        return render_template('login.html',
                               message="Неправильный логин или пароль",)
    return render_template('login.html')


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@blueprint.route('/registration', methods=['GET', 'POST'])
def reg_run():
    if request.method == 'POST':
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == request.form['email']).first():
            return render_template('registration.html', title='Регистрация',
                                   message="Такой пользователь уже есть")
        user = User()
        print(request.form['email'], request.form['password'])
        user.name = request.form['name']
        user.email = request.form['email']
        user.set_password(request.form['password'])
        session = db_session.create_session()
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template("registration.html")
