import csv

from webapp.db import db_session
from webapp.model import Links, Tarif


# читаем csv файл и на выходе получаем словарь с нужными полями
def read_csv_link(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['order',
                  'mobile_operator_name',
                  'tarif_name',
                  'page_link']
        reader = csv.DictReader(f, fields, delimiter=',', )
        link_data = []
        for row in reader:
            link_data.append(row)
        return link_data


def save_links_data(data):
    new_links = []
    for row in data:
        new_link = {'mobile_operator_name': row['mobile_operator_name'],
                    'tarif_name': row['tarif_name'],
                    'page_link': row['page_link']
                    }
        new_links.append(new_link)

    try:
        db_session.bulk_insert_mappings(Links, new_links, return_defaults=True)
        db_session.commit()
    finally:
        db_session.close()
    return new_links


# читаем csv файл и на выходе получаем словарь с нужными полями
def read_csv_tarif(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['order',
                  'mobile_operator_name',
                  'tarif_name',
                  'price',
                  'phone_internet_quantity',
                  'unlim_phone_internet',
                  'phone_minutes_quantity',
                  'unlim_phone_minutes',
                  'phone_sms_quantity',
                  'social_offer_price',
                  'messenger_price',
                  'music_offer_price',
                  'video_offer_price',
                  'stream_offer_price',
                  'ext_information']
        reader = csv.DictReader(f, fields, delimiter=',', )
        tarif_data = []
        for row in reader:
            row['unlim_phone_internet'] = bool(row['unlim_phone_internet'])
            row['unlim_phone_minutes'] = bool(row['unlim_phone_minutes'])
            row['price'] = int(row['price'])
            row['phone_internet_quantity'] = int(row['phone_internet_quantity'])
            row['phone_minutes_quantity'] = int(row['phone_minutes_quantity'])
            row['phone_sms_quantity'] = int(row['phone_sms_quantity'])
            row['social_offer_price'] = int(row['social_offer_price'])
            row['messenger_price'] = int(row['messenger_price'])
            row['music_offer_price'] = int(row['music_offer_price'])
            row['video_offer_price'] = int(row['video_offer_price'])
            row['stream_offer_price'] = int(row['stream_offer_price'])
            tarif_data.append(row)
        return tarif_data


def save_tarif_data(data, links):
    new_tarifs_data = []
    for row in data:
        new_tarif = {'mobile_operator_name': row['mobile_operator_name'],
                     'tarif_name': row['tarif_name'],
                     'price': row['price'],
                     'phone_internet_quantity': row['phone_internet_quantity'],
                     'unlim_phone_internet': row['unlim_phone_internet'],
                     'phone_minutes_quantity': row['phone_minutes_quantity'],
                     'unlim_phone_minutes': row['unlim_phone_minutes'],
                     'phone_sms_quantity': row['phone_sms_quantity'],
                     'social_offer_price': row['social_offer_price'],
                     'messenger_price': row['messenger_price'],
                     'music_offer_price': row['music_offer_price'],
                     'video_offer_price': row['video_offer_price'],
                     'stream_offer_price': row['stream_offer_price'],
                     'ext_information': row['ext_information']
                     }
        new_tarif['link_id'] = get_link_id(row['tarif_name'], links)
        new_tarifs_data.append(new_tarif)
    try:
        db_session.bulk_insert_mappings(Tarif, new_tarifs_data)
        db_session.commit()
    finally:
        db_session.close()
    return new_tarifs_data


def get_link_id(tarif_name, links):
    for row in links:
        if row['tarif_name'] == tarif_name:
            return row['id']
    return None


if __name__ == '__main__':
    data_links = read_csv_link('links.csv')
    links = save_links_data(data_links)
    data_tarifs = read_csv_tarif('input_data_from.csv')
    save_tarif_data(data_tarifs, links)
