import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db, cli



migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

cli.register_app(app)

if __name__ == "__main__":
    manager.run()