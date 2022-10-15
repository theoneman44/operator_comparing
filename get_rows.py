from webapp import create_app
from webapp.tarifs_db import read_csv_tarif
from webapp.links_db import read_csv_link

app = create_app()
with app.app_context():
    read_csv_tarif('input_data_from.csv')
    read_csv_link('links.csv')
