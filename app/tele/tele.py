import app
from app import db

from flask import (
    Blueprint, request, render_template, make_response, abort, session
)

tele = Blueprint('tele', __name__)


@tele.route('/')
@tele.route('/telecomm')
def index():
    return render_template('tele/index.html',
                            title='tele'
                            )