from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField


class QsForm(FlaskForm):
    option = RadioField('Label', choices=[])
    submit = SubmitField('Confirm')
