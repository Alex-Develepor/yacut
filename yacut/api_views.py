import re
from http import HTTPStatus

from flask import jsonify, request

from settings import MAX_CUSTOM_LENGTH, REGULAR
from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_uniq_short_id


@app.route('/api/id/', methods=['POST'])
def api_get_link():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    original = data.get('url')
    if not original:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    short = data.get('custom_id')
    if short:
        if len(short) > MAX_CUSTOM_LENGTH or not re.match(REGULAR, short):
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
        if URLMap.query.filter_by(short=short).first():
            raise InvalidAPIUsage(f'Имя "{short}" уже занято.')
    else:
        short = get_uniq_short_id()
    link = URLMap(
        original=original,
        short=short
    )
    db.session.add(link)
    db.session.commit()
    return jsonify(link.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_original_url(short):
    original_url = URLMap.query.filter_by(short=short).first()
    if not original_url:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': original_url.original}), HTTPStatus.OK
