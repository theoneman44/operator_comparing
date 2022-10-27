import csv

from webapp.mobile.models import Links
from webapp.mobile.models import db


# читаем csv файл и на выходе получаем словарь с нужными полями
def read_csv_link(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['order',
                  'mobile_operator_name',
                  'tarif_name',
                  'page_link'
                  ]
        reader = csv.DictReader(f, fields, delimiter=',', )
        for row in reader:
            save_link_data(row)


def save_link_data(data):
    new_link = Links(mobile_operator_name=data['mobile_operator_name'],
                     tarif_name=data['tarif_name'],
                     page_link=data['page_link']
                     )
    db.session.add(new_link)
    db.session.commit()


if __name__ == '__main__':
    read_csv_link('links.csv')
