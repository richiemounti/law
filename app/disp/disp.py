import app
from app import db

from flask import (
    Blueprint, request, render_template, make_response, abort, session
)

disp = Blueprint('disp', __name__)

@disp.route('/')
@disp.route('/dispute')
def index():
    return render_template(
        'disp/index.html',
        title='disp'
    )
