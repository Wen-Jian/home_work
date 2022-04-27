import pdb
from flask import Flask
import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'app/'))
from flask_cors import CORS
from api.v1.tasks import tasksRoute
from db import db
from flask_migrate import Migrate
import yaml
from yaml import Loader

main = Flask(__name__)
main.register_blueprint(tasksRoute)
Migrate(main, db)

env_var = 'development' if os.environ.get('PYTEST_CURRENT_TEST') else 'test'

main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
with open('config/database.yaml') as db_info:
    info_dict = yaml.load(db_info, Loader=Loader)
    main.config['SQLALCHEMY_DATABASE_URI'] = info_dict[env_var]['db_url']

CORS(main)

db.init_app(main)

@main.after_request # blueprint can also be app~~
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'test'
    main.run(port=5000, debug=True)
    