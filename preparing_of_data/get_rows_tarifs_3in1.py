from webapp import create_app
from tarifs_3in1_db import read_csv_tarif_3in1

app = create_app()
with app.app_context():
    read_csv_tarif_3in1('input_data_3.csv')
