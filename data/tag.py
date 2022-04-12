import sqlalchemy
from data.db_session import SqlAlchemyBase


class Tag(SqlAlchemyBase):
    __tablename__ = 'tag'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    tag = sqlalchemy.Column(sqlalchemy.VARCHAR)



