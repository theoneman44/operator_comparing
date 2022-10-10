from webapp import create_app
from webapp.tarifs_db import read_csv

app = create_app()
with app.app_context():
    read_csv('input_data_from.csv')
