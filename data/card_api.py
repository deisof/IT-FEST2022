from asyncio.windows_events import NULL
import flask
from flask import render_template, request, Response, abort, make_response, url_for
from flask_login import current_user, login_required
from sqlalchemy import null
from werkzeug.utils import redirect
from data import db_session
from data.card import Card
from data.tag import Tag
import string
import secrets
from flask import send_file
from main import app
import sqlite3

blueprint = flask.Blueprint('card_api', __name__, template_folder='templates')


@blueprint.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@blueprint.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    session = db_session.create_session()
    cards = session.query(Card).filter(
        Card.id_creator == current_user.id).all()
    sp = session.query(Card).all()
    card_done = session.query(Card).filter(
        Card.id_creator == current_user.id, Card.is_finished == True).all()
    return render_template("profile.html", cards=cards, card_done=card_done)


# @blueprint.route("/shop", methods=['GET', 'POST'])
# @login_required
# def shop():
#     return render_template("shop.html")


@blueprint.route("/catalog", methods=['GET', 'POST'])
@login_required
def catalog():
    return render_template("catalog.html")


@blueprint.route('/add_card', methods=['GET', 'POST'])
@login_required
def add_card():
    session = db_session.create_session()
    if request.method == 'POST':
        db_sess = db_session.create_session()

        card = Card()
        card.information = request.form['info']
        tag_id = session.query(Tag).filter(
            Tag.tag == request.form['tag_sel']).first()
        card.id_tag = tag_id.id
        card.id_creator = current_user.id

        session.add(card)
        session.commit()

        return redirect('/card_img/' + str(card.id))
    return render_template("add_card.html")


@blueprint.route('/card_img/<int:Card_id>', methods=['POST', 'GET'])
def sample_file_upload(Card_id):
    if request.method == 'POST':
        session = db_session.create_session()
        card = session.query(Card).filter(Card.id == Card_id).first()
        file = request.files['file']
        img = file.read()
        
        binary = sqlite3.Binary(img)
        print(binary)
        card.img_adress = binary

        session.commit()
        return redirect('/profile')
    return render_template("card_img.html")



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


# @blueprint.route("/active")
# def active():
#     session = db_session.create_session()
#     Card_st = session.query(Card).filter(Card.login_student == current_user.login, Card.is_finished == 0).all()
#     Card_te = session.query(Card).filter(Card.login_teacher == current_user.login, Card.is_finished == 0).all()
#     return render_template('active.html', Card_st=Card_st, Card_te=Card_te)


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
