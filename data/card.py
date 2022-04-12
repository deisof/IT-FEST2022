import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase


class Card(SqlAlchemyBase):
    __tablename__ = 'card'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    img_adress = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=False)
    information = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=True)
    id_creator = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    user = orm.relation('User')
    id_tag = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("tag.id"))
    tag = orm.relation('Tag')
