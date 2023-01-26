from http import HTTPStatus

from flask import flash, redirect, render_template

from . import app, db
from .forms import LinksForm
from .models import URLMap
from .utils import get_uniq_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = LinksForm()
    if form.validate_on_submit():
        custom_link = form.custom_id.data
        if not custom_link:
            custom_link = get_uniq_short_id()
        if URLMap.query.filter_by(short=custom_link).first():
            flash(f'Имя {custom_link} уже занято!')
            return render_template('main.html', form=form)
        link = URLMap(
            original=form.original_link.data,
            short=custom_link
        )
        db.session.add(link)
        db.session.commit()
        return render_template('main.html', form=form, short=custom_link), HTTPStatus.OK
    return render_template('main.html', form=form)


@app.route('/<string:short>')
def redirect_view(short):
    original_url = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(original_url.original)
