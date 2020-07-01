import app
from app import db

from flask import (
    Blueprint, request, render_template, make_response, abort, session
)

team = Blueprint('team', __name__)

@team.route('/')
@team.route('/teams')
def index():
    return render_template('team/index.html',
                            title='team'
                            )