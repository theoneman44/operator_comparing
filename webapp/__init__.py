from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from webapp.model import Tarif, Links

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def index():
        request_data = request.args
        title = "Предлагаемые тарифы"

        if 'phone_internet_quantity' and 'phone_minutes_quantity' and 'phone_sms_quantity' in request_data.keys():
            tarifs = Tarif.query.filter(Tarif.phone_internet_quantity == request_data['phone_internet_quantity'],
                                        Tarif.phone_minutes_quantity == request_data['phone_minutes_quantity'],
                                        Tarif.phone_sms_quantity == request_data['phone_sms_quantity']
                                        ).all()
            tarifs_list = []
            if tarifs:
                for tarif in tarifs.link:
                    tarifs_list.append(f"{tarifs.name} - {tarif.link}")

            print(tarifs_list)
        else:
            tarifs_list = 'Настройте фильтр и увидите рекомендации'
        return render_template('index.html', page_title=title, tarifs_list=tarifs_list)

    return app
