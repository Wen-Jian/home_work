import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'app/'))
from app import main
# from flask_migrate import Migrate
# from app import db

from waitress import serve

# manager = Manager(main)
# manager.add_command('runserver', serve(main, port=5000))

# @manager.shell
# def make_shell_context():
#     return dict(app=main, User=User)

if __name__ == '__main__':
    # manager.run()
    print('server is hosting on 5000 prot')
    os.environ['flask_env'] = 'production'
    serve(main, port=5000)