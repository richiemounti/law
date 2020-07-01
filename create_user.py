#!/usr/bin/env python3
from getpass import getpass
import sys

from flask import current_app
from app import app, bcrypt, db
from app.models import User, Permissions, Role

def main():
    """
    Main entrypoint for script
    """
    with app.app_context():
        db.metadata.create_all(db.engine)
        if User.query.all():
            print('A user already exists! Create another?')
            create = input()
            if create == 'n':
                return
        
        Role.insert_roles()
        print('Enter Username:')
        username = input()
        password = getpass()
        assert password == getpass('Password (again):')

        user = User(username=username, 
                    password=password, 
                    role=Role.query.filter_by(permissions=Permissions.ADMINISTER).first()
                    )
        
        db.session.add(user)
        db.session.commit()
        print('User added.')


if __name__ == "__main__":
    sys.exit(main())
