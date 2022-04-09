import sqlalchemy
from data.db_session import SqlAlchemyBase


class Card(SqlAlchemyBase):
    __tablename__ = 'card'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    img_adress = sqlalchemy.Column(sqlalchemy.VARCHAR)
    information = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=True)
    id_tag = sqlalchemy.Column(sqlalchemy.Integer)
    id_creator = sqlalchemy.Column(sqlalchemy.Integer)


