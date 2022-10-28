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
        if request_data:
            tarifs_list = queries(request_data)
            return render_template('mobile/mobile.html', title=title, tarifs_list=tarifs_list, tarifs_list_len=len(tarifs_list))
        else:
            return render_template('mobile/mobile.html', title=title)

    return app
