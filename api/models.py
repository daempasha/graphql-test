import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from database import Base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(30))
    fullname = sa.Column(sa.String(100))