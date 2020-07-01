import app
from app import db

from flask import (
    Blueprint, request, render_template, make_response, abort, session
)

commer = Blueprint('commer', __name__)

@commer.route('/')
@commer.route('/commercial')
def index():
    return render_template('commer/index.html',
                            title='commer'
                            )