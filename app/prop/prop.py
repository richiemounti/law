import app
from app import db

from flask import (
    Blueprint, request, render_template, make_response, abort, session
)

prop = Blueprint('prop', __name__)

@prop.route('/')
@prop.route('/property')
def index():
    return render_template('prop/index.html',
                            title='prop'
                            )