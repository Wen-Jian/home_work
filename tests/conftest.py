from app.models.task import Task
# import os
# os.environ['flask_env'] = 'test'
# import pdb; pdb.set_trace()
from app import main
import pytest
import yaml
from yaml import Loader
from app.db import db 


with open('config/database.yaml') as db_info:
    info_dict = yaml.load(db_info, Loader=Loader)
    main.config['SQLALCHEMY_DATABASE_URI'] = info_dict['test']['db_url']




@pytest.fixture(scope='module')
def new_task():
    task = Task('Test Task')
    db.session.add(task)
    db.session.commit()
    return task

@pytest.fixture(scope='module')
def test_client():
    with main.test_client() as testing_client:
        with main.app_context():
            yield testing_client