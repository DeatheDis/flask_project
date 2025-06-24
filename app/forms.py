from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    email = StringField('Email Агента', validators=[DataRequired(message='Это обязательное поле'),
                                                    Email('Некорректный email')])
    title = StringField('Тема')
    message = TextAreaField('Сообщение', validators=[DataRequired(message='Это обязательное поле')])
    submit = SubmitField('Отправить')


class AgentForm(FlaskForm):
    code_name = StringField('Кодовое Имя: ', validators=[DataRequired(message='Это обязательное поле'),
                                                         Length(min=2, max=50)])
    agent_number = StringField('Номер Агента: ', validators=[Length(min=1, max=20)])
    agent_email = StringField('Email Агента', validators=[DataRequired(message='Это обязательное поле'),
                                                          Email('Некорректный email')])
    agent_access = SelectField('Уровень доступа', choices=[
        ('Секретно', 'Секретно'),
        ('Совершенно секретно', 'Совершенно секретно'),
        ('Особой важности', 'Особой важности'),
    ], validators=[DataRequired('Выберите уровень секретности')])

    submit = SubmitField()
