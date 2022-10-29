from flask import Flask, render_template, request

from webapp.mobile.models import db as db1
from webapp.all_in.models import db as db2
from webapp.mobile.queries import queries


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db1.init_app(app)
    db2.init_app(app)

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