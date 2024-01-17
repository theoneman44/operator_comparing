from flask import flash, Flask, render_template, request, send_from_directory
from flask.wrappers import Response
from webapp.mobile.models import db
from webapp.mobile.queries import queries as queries1
from webapp.all_in.queries import queries as queries2


def create_app() -> str | Flask:
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    # db2.init_app(app)

    @app.route("/")
    def index() -> str:
        request_data = request.args
        title = "Сравнение мобильных операторов"
        if request_data:
            tarifs_list = queries1(request_data)
            if len(tarifs_list) == 0:
                flash('По указанным параметрам не найдено ни одного тарифа. Попробуйте немного изменить значения.')
            return render_template('mobile/mobile.html',
                                   title=title,
                                   tarifs_list=tarifs_list,
                                   tarifs_list_len=len(tarifs_list),
                                   request_data=request_data
                                   )
        else:
            return render_template('mobile/mobile.html', title=title, request_data=request_data)

    @app.route("/images/<path:name>")
    def download_file(name: str) -> Response:
        return send_from_directory(
            app.config['UPLOAD_FOLDER'], name, as_attachment=True
        )

    @app.route("/all_in")
    def index1() -> str:
        request_data = request.args
        title = "Сравнение мобильных операторов"
        if request_data:
            tarifs_list = queries2(request_data)
            if len(tarifs_list) == 0:
                flash('По указанным параметрам не найдено ни одного тарифа. Попробуйте немного изменить значения.')
            return render_template('all_in/all_in.html',
                                   title=title, tarifs_list=tarifs_list,
                                   tarifs_list_len=len(tarifs_list),
                                   request_data=request_data
                                   )
        else:
            return render_template('all_in/all_in.html', title=title, request_data=request_data)

    return app
