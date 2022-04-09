from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, ValidationError


class TestForm(FlaskForm):
    login_student = StringField("Логин ученика", validators=[DataRequired()])
    login_teacher = StringField("Логин учителя")
    description = StringField("Название теста", validators=[DataRequired()])
    is_finished = BooleanField("Пройден ли тест?")
    result = StringField("Ссылка на файл")
    submit = SubmitField('Готово')


class Ready(FlaskForm):
    submit_ready = SubmitField('Завершить')


class Send(FlaskForm):
    submit_send = SubmitField('Отправить отчёт')
