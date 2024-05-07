from database import session
from models import User
from faker import Faker
import random
from flask import jsonify
fake = Faker()

def create_response(key: str, objects: list):
    return jsonify({key: convert_sqlalchemy_object_to_json(objects)})


def convert_sqlalchemy_object_to_json(objects: list):
    dict_list = list(map(lambda object: object.__dict__, objects))

    # Drop classes
    for row in dict_list:
        del row["_sa_instance_state"]

    return dict_list

def truncate_table(model):
    """Remove all data from a model."""
    session.query(model).delete()
    session.commit()
    return True

def _get_table_count(model):
    """Get a count of the tables"""
    return session.query(model).count()

def _seed_users(amount: int = 50):
    users = []

    count = _get_table_count(User)

    if count > 0:
        return

    ran_number = random.random() * 34326
    for i in range(amount):
        users.append(User(id=ran_number+i, name=fake.name(), fullname=fake.name()))
    session.add_all(users)
    session.commit()

def seed_db():
    _seed_users()
