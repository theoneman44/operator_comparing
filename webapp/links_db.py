import csv

from webapp.model import Links, db


# читаем csv файл и на выходе получаем словарь с нужными полями
def read_csv_link(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['order',
                  'mobile_operator_name',
                  'tarif_name',
                  'page_link']
        reader = csv.DictReader(f, fields, delimiter=',', )

        for row in reader:
            save_links_data(row)


def save_links_data(data):
    new_link = Links(mobile_operator_name=data['mobile_operator_name'],
                    tarif_name=data['tarif_name'],
                    page_link=data['page_link']
                    )
    try:
        db.session.add(new_link)
        db.session.commit()
    finally:
        db.session.close()
