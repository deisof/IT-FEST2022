import flask
from flask import render_template, request, Response, abort
from flask_login import current_user, login_required
from werkzeug.utils import redirect
from data import db_session
from data.card import Card
import string
import secrets
from flask import send_file

blueprint = flask.Blueprint('card_api', __name__, template_folder='templates')


@blueprint.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


# @blueprint.route("/shop", methods=['GET', 'POST'])
# @login_required
# def shop():
#     return render_template("shop.html")


# @blueprint.route("/check")
# def Card_func():
#     return render_template('check.html')


# @blueprint.route("/Carding/<int:Card_id>", methods=['GET', 'POST'])
# def Carding(Card_id):
#     form = Ready()
#     session = db_session.create_session()
#     Card = session.query(Card).filter(Card.id == Card_id).first()

#     if request.method == "POST":

#         if form.submit_ready.data:
#             Card.is_finished = 1
#             alphabet = string.ascii_letters + string.digits
#             password = ''.join(secrets.choice(alphabet) for i in range(6))
#             Card.result = f'data_cam/{password}.txt'
#             session.commit()

#         return redirect('/history')
#     return render_template('Carding.html', form=form, Card=Card)


# @blueprint.route("/about")
# def about():
#     return render_template('about.html')


# @blueprint.route("/help")
# def helper():
#     return render_template('help.html')


# @blueprint.route("/active")
# def active():
#     session = db_session.create_session()
#     Card_st = session.query(Card).filter(Card.login_student == current_user.login, Card.is_finished == 0).all()
#     Card_te = session.query(Card).filter(Card.login_teacher == current_user.login, Card.is_finished == 0).all()
#     return render_template('active.html', Card_st=Card_st, Card_te=Card_te)


# @blueprint.route("/history")
# def history():
#     session = db_session.create_session()
#     Card = session.query(Card).filter(Card.login_student == current_user.login, Card.is_finished == 1).all()
#     Card1 = session.query(Card).filter(Card.login_teacher == current_user.login, Card.is_finished == 1).all()
#     Card.extend(Card1)

#     return render_template('history.html', Card=Card)


# @blueprint.route('/add_Card', methods=['GET', 'POST'])
# @login_required
# def add_Card():
#     form = CardForm()
#     session = db_session.create_session()
#     Card = Card()
#     if form.validate_on_submit():
#         Card.login_student = form.login_student.data
#         Card.login_teacher = current_user.login
#         Card.description = form.description.data
#         Card.is_finished = 0

#         session.add(Card)
#         session.commit()

#         return redirect('/active')
#     return render_template('add.html', form=form)


# @blueprint.route('/edit_Card/<int:Card_id>', methods=['GET', 'POST'])
# @login_required
# def edit_job(Card_id):
#     form = CardForm()
#     session = db_session.create_session()
#     Card = session.query(Card).filter(Card.id == Card_id, Card.login_teacher == current_user.login).first()
#     if request.method == "GET":
#         if Card:
#             form.login_student.data = Card.login_student
#             form.description.data = Card.description
#         else:
#             abort(404)
#     if form.validate_on_submit():
#         if Card:
#             Card.login_student = form.login_student.data
#             Card.login_teacher = current_user.login
#             Card.description = form.description.data
#             Card.is_finished = 0

#             session.commit()
#             return redirect('/active')
#         else:
#             abort(404)
#     return render_template('add.html', title='Редактирование тестирования', form=form)


# @blueprint.route('/delete_Card/<int:Card_id>', methods=['GET', 'POST'])
# @login_required
# def Card_delete(Card_id):
#     session = db_session.create_session()
#     Card = session.query(Card).filter(Card.id == Card_id, Card.login_teacher == current_user.login).first()
#     if Card:
#         session.delete(Card)
#         session.commit()
#     else:
#         abort(404)
#     return redirect('/active')


# @blueprint.route('/data_cam/<path:filename>', methods=['GET', 'POST'])
# @login_required
# def download(filename):
#     return send_file(filename)
