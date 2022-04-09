import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase


class Tag(SqlAlchemyBase):
    __tablename__ = 'tag'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    tag = sqlalchemy.Column(sqlalchemy.VARCHAR)
    user = orm.relation("User", back_populates='privilege')


