from flask_wtf import FlaskForm
from settings import MAX_CUSTOM_LENGTH, REGULAR
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp


class LinksForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    URL(message='Введите ссылку целиком')]
    )
    custom_id = StringField(
        'Введите свой вариант короткой ссылки',
        validators=[Length(max=MAX_CUSTOM_LENGTH, message='Длинна ссылки должна быть не больше 16 символов'),
                    Regexp(REGULAR, message='Только латинские буквы и цифры'),
                    Optional()]
    )
    sumbit = SubmitField('Создать')
