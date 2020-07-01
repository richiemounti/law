from datetime import datetime
from app.extensions import bcrypt, db, login
from flask_login import UserMixin, AnonymousUserMixin
from flask_sqlalchemy import BaseQuery
from sqlalchemy_searchable import SearchQueryMixin, make_searchable
from sqlalchemy_utils.types import TSVectorType

db.configure_mappers()
make_searchable(db.metadata)

class Permissions:
    GENERAL = 0
    ADMINISTER = 1



class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(1000))
    image_url = db.Column(db.String(140))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def from_dict(self, data):
        for field in ['title', 'description', 'image_url','category_id', ]:
            if field in data:
                setattr(self, field, data[field])
    
    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image_url': self.image_url,
            'category_id': self.category_id
        }

        return data             

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    index = db.Column(db.String(64))
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permissions.GENERAL, 'main', True),
            'Administrator': (Permissions.ADMINISTER, 'admin', False)
        }

        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.index = roles[r][1]
            role.default = roles[r][2]
            db.session.add(role)
        db.session.commit()


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.Binary(128), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, username, role=None, password=None, **kwargs):
        super(User, self).__init__(**kwargs)
        if role:
            self.role = role
        db.Model.__init__(self, username=username, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None
    
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)
    
    def check_password(self, value):
        self.password = bcrypt.check_password_hash(self.password, value)
    
    def can(self, permissions):
        return self.role.permissions >= permissions
    
    def is_admin(self):
        return self.can(Permissions.ADMINISTER)
    

class AnonymousUser(AnonymousUserMixin):
    def can(self, _):
        return False

    def is_admin(self):
        return False




class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    blog_items = db.relationship(
        'Blog',
        backref='category'
    )


@login.user_loader
def load_user(id):
    return User.query.get(int(id))