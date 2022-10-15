import csv


# читаем csv файл и на выходе получаем словарь с нужными полями
def read_csv(filename):
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
        # save_tarif_data(tarif_data)


'''
def excel(filename):
    # Читаем файл в переменную. Тип данных DataFrame.
    reader = pd.read_excel(filename)
    # Указываем значения полей
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
    data = pd.DataFrame(reader, columns=fields)
    data.to_sql("data", engine)
    # Пока не работает


# загружаем полученный словарь в БД
def save_tarif_data(data):
    db_session.bulk_insert_mappings(Tarif, data)
    db_session.commit()
'''

if __name__ == '__main__':
    read_csv('input_data_from.csv')
    # excel(XLSX)
