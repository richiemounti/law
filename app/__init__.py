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

from app.admin.admin import admin
from app.api import api
from app.blog.blog import blog
from app.main.main import intro
from app.commer.commer import commer
from app.disp.disp import disp
from app.employ.employ import employ
from app.priv.priv import priv
from app.prop.prop import prop
from app.team.team import team
from app.tele.tele import tele

from app.accounts.account import account


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
app.register_blueprint(account)