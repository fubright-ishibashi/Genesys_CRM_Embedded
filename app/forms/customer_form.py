from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,SelectField
from wtforms.validators import DataRequired, Email

class CustomerForm(FlaskForm):
    id = StringField('id', render_kw={"class": "form-control", "size": 32}, validators=[DataRequired()])
    customer_name = StringField('顧客名', render_kw={"class": "form-control", "size": 32}, validators=[DataRequired()])
    division_name = StringField('部署名', render_kw={"class": "form-control", "size": 32}, validators=[DataRequired()])
    manager_name = StringField('担当者名', render_kw={"class": "form-control", "size": 32}, validators=[DataRequired()])
    post_code = StringField('郵便番号', render_kw={"class": "form-control", "size": 32}, validators=[DataRequired()])
    telephone_number = StringField('電話番号', render_kw={"class": "form-control", "size": 32}, validators=[DataRequired()])
    cellphone_number = StringField('携帯電話', render_kw={"class": "form-control", "size": 32}, validators=[DataRequired()])
    address = StringField('住所', render_kw={"class": "form-control", "size": 32}, validators=[DataRequired()])
    fax_address = StringField('FAX', render_kw={"class": "form-control", "size": 32}, validators=[DataRequired()])
    mail_address = StringField('メールアドレス', render_kw={"class": "form-control", "size": 32}, validators=[DataRequired(), Email()])
    customer_lank = SelectField(
        '顧客ランク', 
        choices=[('Z', 'Open this select menu'),('A', 'Aランク'), ('B', 'Bランク'), ('C', 'Cランク')], 
        render_kw={"class": "form-select form-control"}
    )
    memo = TextAreaField('メモ', render_kw={"class": "form-control", "rows": 4}, validators=[DataRequired()])
    submit = SubmitField('登録')
