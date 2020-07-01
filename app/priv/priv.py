import app
from app import db

from flask import (
    Blueprint, request, render_template, make_response, abort, session
)

priv = Blueprint('priv', __name__)

@priv.route('/')
@priv.route('/private')
def index():
    return render_template('priv/index.html',
                            title='priv'
                            )