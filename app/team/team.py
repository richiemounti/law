import app
from app import db
from app.messages.forms import MessageForm
from app.models import Category


from flask import (
    Blueprint, request, render_template, make_response, abort, session
)

team = Blueprint('team', __name__)

@team.route('/')
@team.route('/teams')
def index():
    categories = Category.query.all()
    form = MessageForm()
    form.category_id.choices = [(c.id, c.name) for c in categories]
    return render_template('team/index.html',
                            title='team',
                            form=form
                            )