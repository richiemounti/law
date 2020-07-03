import app
from app import db, mail


from app.models import Category

from flask_mail import Message
from flask import (
    Blueprint, request, render_template, make_response, abort, session, flash
)

from app.messages.forms import MessageForm

intro = Blueprint('intro', __name__, template_folder='templates')

from app.main import Views


@intro.route('/')
@intro.route('/index')
def index():
    categories = Category.query.all()
    form = MessageForm()
    form.category_id.choices = [(c.id, c.name) for c in categories]
    return render_template('intro/index.html',
                            title='main',
                            form=form
                            )

@intro.route('/submit', methods=['GET', 'POST'])
def submit():
    categories = Category.query.all()
    form = MessageForm()
    form.category_id.choices = [(c.id, c.name) for c in categories]
    
    if form.validate_on_submit():

        msg = Message(subject='Enquiry',
                      sender= 'guyalawapp@gmail.com',
                      recipients=['babtdaddy67@gmail.com'],
                      html=render_template('intro/_contact_form.html',form=form)
                        )
        
        mail.send(msg)
        flash('message sent', 'success')
    
    return render_template('intro/index.html',
                            form=form,
                            msg=msg,
                            title="message item"
                            )