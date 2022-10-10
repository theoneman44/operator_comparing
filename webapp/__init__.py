from flask import Flask, render_template

from webapp.model import Tarif, db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)


    @app.route("/")
    def index():
        title = "Предлагаемые тарифы"
        tarifs_list = Tarif.query.order_by(Tarif.price.desc()).all()
        return render_template('index.html', page_title=title, tarifs_list=tarifs_list)

    return app
    