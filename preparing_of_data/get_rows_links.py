from webapp import create_app
from links_db import read_csv_link

app = create_app()
with app.app_context():
    read_csv_link('links.csv')
