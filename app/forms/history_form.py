from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class HistoryForm(FlaskForm):
    history_type1 = StringField('history_type1', validators=[DataRequired()])
    history_type2 = StringField('history_type2', validators=[DataRequired()])
    inquiry_details = StringField('inquiry_details', validators=[DataRequired()])
    contact_person = StringField('contact_person', validators=[DataRequired()])
    status = StringField('status', validators=[DataRequired()])
    submit = SubmitField('Add History')
