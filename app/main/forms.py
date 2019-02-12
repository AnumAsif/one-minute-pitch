from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    message = TextAreaField('Movie review',validators=[Required()])
    submit = SubmitField('Submit')
