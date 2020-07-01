from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    SubmitField
)
from wtforms.validators import DataRequired

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    image_url = StringField('Image Upload', validators=[DataRequired()])
    category_id = SelectField('Category', coerce=int)
    submit = SubmitField('Save')
