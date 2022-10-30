from flask import Flask, render_template, request, send_from_directory

from webapp.mobile.models import db as db1
from webapp.all_in.models import db as db2
from webapp.mobile.queries import queries as queries1
from webapp.all_in.queries import queries as queries2


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
            tarifs_list = queries1(request_data)
            return render_template('mobile/mobile.html', title=title, tarifs_list=tarifs_list, tarifs_list_len=len(tarifs_list))
        else:
            return render_template('mobile/mobile.html', title=title)
    
    @app.route("/images/<path:name>")
    def download_file(name):
        return send_from_directory(
        app.config['UPLOAD_FOLDER'], name, as_attachment=True
    )

    @app.route("/all_in")
    def index1():
        request_data = request.args
        title = "Сравнение мобильных операторов"
        if request_data:
            tarifs_list = queries2(request_data)
            return render_template('all_in/all_in.html', title=title, tarifs_list=tarifs_list, tarifs_list_len=len(tarifs_list))
        else:
            return render_template('all_in/all_in.html', title=title)

    return app