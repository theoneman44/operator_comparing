import csv

from webapp.models import Links, Tarif, db


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
            save_tarif_data(row)


def save_tarif_data(data):
    new_tarif = Tarif(mobile_operator_name=data['mobile_operator_name'],
                      tarif_name=data['tarif_name'],
                      price=data['price'],
                      phone_internet_quantity=data['phone_internet_quantity'],
                      unlim_phone_internet=data['unlim_phone_internet'],
                      phone_minutes_quantity=data['phone_minutes_quantity'],
                      unlim_phone_minutes=data['unlim_phone_minutes'],
                      phone_sms_quantity=data['phone_sms_quantity'],
                      social_offer_price=data['social_offer_price'],
                      messenger_price=data['messenger_price'],
                      music_offer_price=data['music_offer_price'],
                      video_offer_price=data['video_offer_price'],
                      stream_offer_price=data['stream_offer_price'],
                      ext_information=data['ext_information'],
                      link_id=get_link_id(data['tarif_name'])
                      )
    db.session.add(new_tarif)
    db.session.commit()


def get_link_id(tarif_name):
    link = Links.query.filter(Links.tarif_name == tarif_name).first()
    return link.id


if __name__ == '__main__':
    read_csv_tarif('input_data_from.csv')
