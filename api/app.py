from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS
from database import init_db, session

from models import User
from schema import schema

from utils import seed_db, truncate_table
from flask import jsonify

from utils import create_response

app = Flask(__name__)
app.debug = True

CORS(app)
init_db()
seed_db()

    
app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))

query = '''
    query {
      allUsers {
        edges { 
            node {
                id
                name
            }
        }
      }
    }
'''
result = schema.execute(query, context_value={'session': session})

print("result: ", result)

@app.route("/")
def hello():
    users: list[User] = session.query(User).all()

    
    return create_response("users", users)
    

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()