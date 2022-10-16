from flask import Flask, render_template, request

from webapp.db import db
from webapp.models import Tarif, Links
from webapp.queries import queries


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def index():
        request_data = request.args
        title = "Предлагаемые тарифы"

        if 'phone_sms_quantity' not in request_data.keys():
            tarifs_list = ['Настройте фильтр и увидите рекомендации']
            return render_template('index.html', page_title=title, tarifs_list=tarifs_list)
        else:
            tarifs_list = queries(request_data)
            return render_template('index2.html', page_title=title, tarifs_list=tarifs_list)

    return app
