from flask import Flask, render_template, request, redirect, url_for

from webapp.db import db
from webapp.models import Tarif, Links
from webapp.queries import queries


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def index():
        title = "Сравнение мобильных операторов"
        return render_template('index.html', title = title)

    @app.route("/filters")
    def filters():
        request_data = request.args
        tarifs_list = queries(request_data)
        return render_template('index.html', tarifs_list=tarifs_list)



    return app
