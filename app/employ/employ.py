import app
from app import db

from flask import (
    Blueprint, request, render_template, make_response, abort, session
)

employ = Blueprint('employ', __name__)


@employ.route('/')
@employ.route('/employment')
def index():
    return render_template('employ/index.html',
                            title='employ'                            
                            )