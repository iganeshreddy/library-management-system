from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=150)])
    author = StringField('Author', validators=[DataRequired(), Length(max=100)])
    year = IntegerField('Year', validators=[DataRequired()])
    submit = SubmitField('Submit')
