from webapp.models import Tarif

# mobile_operator_name=0&phone_internet_quantity=0&unlim_phone_internet=0&phone_minutes_quantity=0&unlim_phone_minutes=0&phone_sms_quantity=0&
# social_offer_price=0&messenger_price=0&music_offer_price=0&video_offer_price=0&stream_offer_price=0


def queries(request_result):

    tarifs_list = Tarif.query.filter(Tarif.phone_sms_quantity == request_result['phone_sms_quantity'])

    if request_result['mobile_operator_name'] != '0':
        tarifs_list = tarifs_list.filter(Tarif.mobile_operator_name == request_result['mobile_operator_name'])

    if request_result['unlim_phone_internet'] == '0':
        tarifs_list = tarifs_list.filter(Tarif.phone_internet_quantity == request_result['phone_internet_quantity'])
    elif request_result['unlim_phone_internet'] == '1':
        tarifs_list = tarifs_list.filter(Tarif.unlim_phone_internet == request_result['unlim_phone_internet'])

    if request_result['unlim_phone_minutes'] == '0':
        tarifs_list = tarifs_list.filter(Tarif.phone_minutes_quantity == request_result['phone_minutes_quantity'])
    elif request_result['unlim_phone_minutes'] == '1':
        tarifs_list = tarifs_list.filter(Tarif.unlim_phone_minutes == request_result['unlim_phone_minutes'])

    tarifs_list = tarifs_list.all()

    return tarifs_list
