import csv
from webapp.db import db

from webapp.all_in.models import Tarif_3in1


# читаем csv файл и на выходе получаем словарь с нужными полями
def read_csv_tarif(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['order',
                  'mobile_operator_name',
                  'tarif_name',
                  'price',
                  'phone_internet_qty',
                  'phone_minutes_qty',
                  'phone_sms_qty',
                  'social_offer_price',
                  'messenger_price',
                  'music_offer_price',
                  'video_offer_price',
                  'ext_information',
                  'family_num',
                  'internet_speed',
                  'traffic_qty',
                  'channels_qty',
                  'tv_name',
                  'page_link']
        reader = csv.DictReader(f, fields, delimiter=',', )
        for row in reader:
            row['price'] = int(row['price'])
            row['phone_internet_qty'] = int(row['phone_internet_qty'])
            row['phone_minutes_qty'] = int(row['phone_minutes_qty'])
            row['phone_sms_qty'] = int(row['phone_sms_qty'])
            row['social_offer_price'] = int(row['social_offer_price'])
            row['messenger_price'] = int(row['messenger_price'])
            row['music_offer_price'] = int(row['music_offer_price'])
            row['video_offer_price'] = int(row['video_offer_price'])
            row['family_num'] = int(row['family_num'])
            row['internet_speed'] = int(row['internet_speed'])
            row['traffic_qty'] = int(row['traffic_qty'])
            row['channels_qty'] = int(row['channels_qty'])
            save_tarif_data(row)


def save_tarif_data(data):
    new_tarif = Tarif_3in1(mobile_operator_name=data['mobile_operator_name'],
                           tarif_name=data['tarif_name'],
                           price=data['price'],
                           phone_internet_qty=data['phone_internet_qty'],
                           phone_minutes_qty=data['phone_minutes_qty'],
                           phone_sms_qty=data['phone_sms_qty'],
                           social_offer_price=data['social_offer_price'],
                           messenger_price=data['messenger_price'],
                           music_offer_price=data['music_offer_price'],
                           video_offer_price=data['video_offer_price'],
                           ext_information=data['ext_information'],
                           family_num=data['family_num'],
                           internet_speed=data['internet_speed'],
                           traffic_qty=data['traffic_qty'],
                           channels_qty=data['channels_qty'],
                           tv_name=data['tv_name'],
                           page_link=data['page_link']
                           )
    db.session.add(new_tarif)
    db.session.commit()


if __name__ == '__main__':
    read_csv_tarif('input_data_3.csv')
