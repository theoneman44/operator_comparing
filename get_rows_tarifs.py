from webapp import create_app
from tarifs_db import read_csv_tarif

app = create_app()
with app.app_context():
    read_csv_tarif('input_data_from.csv')
