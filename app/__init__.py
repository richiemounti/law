import os
import sys

import config

from app.extensions import (
    bcrypt,
    csrf_protect,
    db,
    login,
    mail
)

from flask import (
    Flask
)



app = Flask(__name__)

app.config.from_object('config.Development')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


bcrypt.init_app(app)
db.init_app(app)
csrf_protect.init_app(app)
login.init_app(app)
mail.init_app(app)

from .admin.admin import admin
from .api import api
from .blog.blog import blog
from .main.main import intro
from .commer.commer import commer
from .disp.disp import disp
from .employ.employ import employ
from .priv.priv import priv
from .prop.prop import prop
from .team.team import team
from .tele.tele import tele
from .admin.login import login


app.register_blueprint(admin)
app.register_blueprint(api)
app.register_blueprint(blog)
app.register_blueprint(intro)
app.register_blueprint(commer)
app.register_blueprint(disp)
app.register_blueprint(employ)
app.register_blueprint(priv)
app.register_blueprint(prop)
app.register_blueprint(team)
app.register_blueprint(tele)
app.register_blueprint(login)