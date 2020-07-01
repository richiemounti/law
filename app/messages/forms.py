from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    SubmitField,
    TextAreaField,
    TextField
)

from wtforms.validators import DataRequired




class MessageForm(FlaskForm):
    name = TextField('NAME', validators=[DataRequired()])
    email = TextField('EMAIL', validators=[DataRequired()])
    category_id = SelectField('Which service do you require', coerce=int)
    description = TextAreaField('MESSAGE', validators=[DataRequired()])
    submit = SubmitField('submit')