from email.policy import default
import sqlalchemy
from sqlalchemy import null, orm
from data.db_session import SqlAlchemyBase
from flask import url_for
from main import app


class Card(SqlAlchemyBase):
    __tablename__ = 'card'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    img_adress = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)
    information = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.BOOLEAN, default=False)
    id_creator = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    user = orm.relation('User')
    id_tag = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("tag.id"))
    tag = orm.relation('Tag')

    def get_img(self):
        img = None
        if not self.__card['img_adress']:
            try:
                with app.open_resource(app.root_path + url_for('static', filename='img/team_foto.jpg'), "rb") as f:
                    img = f.read()
            except FileNotFoundError as e:
                print("Не найден аватар по умолчанию: "+str(e))
        else:
            img = self.__card['img_adress']
 
        return img
