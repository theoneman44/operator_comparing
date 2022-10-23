from flask import Flask, render_template, request

from webapp.db import db
from webapp.queries import queries


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def index():
        request_data = request.args
        title = "Сравнение мобильных операторов"
        tarifs_list = queries(request_data)
        return render_template('index.html', title=title, tarifs_list=tarifs_list)

    return app
