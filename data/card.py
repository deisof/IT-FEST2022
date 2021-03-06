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
