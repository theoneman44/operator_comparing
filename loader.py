import csv
from db import db_session
from model import Tarif


def read_csv(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        fields = ['mobile_operator_name',
                  'tarif_name',
                  'package_offer',
                  'tarif_change',
                  'price',
                  'phone_internet',
                  'phone_minutes',
                  'phone_sms',
                  'social_offer',
                  'music_offer',
                  'video_offer',
                  'stream_offer',
                  'ext_information']
        reader = csv.DictReader(f, fields, delimiter=';')
        tarif_data = []
        for row in reader:
            tarif_data.append(row)
        save_tarif_data(tarif_data)


def save_tarif_data(data):
    db_session.bulk_insert_mappings(Tarif, data)
    db_session.commit()


if __name__ == '__main__':
    read_csv('input_data1.csv')
