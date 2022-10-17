from webapp.models import Tarif

# mobile_operator_name=0&phone_internet_quantity=0&unlim_phone_internet=0&phone_minutes_quantity=0&unlim_phone_minutes=0&phone_sms_quantity=0&
# social_offer_price=0&messenger_price=0&music_offer_price=0&video_offer_price=0&stream_offer_price=0


def queries(request_result):
    condition1 = bool(request_result['mobile_operator_name'] == '0' and request_result['unlim_phone_internet'] == '0' and request_result['unlim_phone_minutes'] == '0')
    condition2 = bool(request_result['mobile_operator_name'] == '0' and request_result['unlim_phone_internet'] == '0' and request_result['unlim_phone_minutes'] == '1')
    condition3 = bool(request_result['mobile_operator_name'] == '0' and request_result['unlim_phone_internet'] == '1' and request_result['unlim_phone_minutes'] == '0')
    condition4 = bool(request_result['mobile_operator_name'] == '0' and request_result['unlim_phone_internet'] == '1' and request_result['unlim_phone_minutes'] == '1')
    condition5 = bool(request_result['mobile_operator_name'] != '0' and request_result['unlim_phone_internet'] == '0' and request_result['unlim_phone_minutes'] == '0')
    condition6 = bool(request_result['mobile_operator_name'] != '0' and request_result['unlim_phone_internet'] == '0' and request_result['unlim_phone_minutes'] == '1')
    condition7 = bool(request_result['mobile_operator_name'] != '0' and request_result['unlim_phone_internet'] == '1' and request_result['unlim_phone_minutes'] == '0')
    condition8 = bool(request_result['mobile_operator_name'] != '0' and request_result['unlim_phone_internet'] == '1' and request_result['unlim_phone_minutes'] == '1')
    if condition1:
        print(1)
        tarifs_list = Tarif.query.filter(Tarif.phone_internet_quantity == request_result['phone_internet_quantity'],
                                         Tarif.phone_minutes_quantity == request_result['phone_minutes_quantity'],
                                         Tarif.phone_sms_quantity == request_result['phone_sms_quantity']
                                         ).all()

        return tarifs_list
    elif condition2:
        print(2)
        tarifs_list = Tarif.query.filter(Tarif.phone_internet_quantity == request_result['phone_internet_quantity'],
                                         Tarif.unlim_phone_minutes == request_result['unlim_phone_minutes'],
                                         Tarif.phone_sms_quantity == request_result['phone_sms_quantity']
                                         ).all()
        return tarifs_list
    elif condition3:
        print(3)
        tarifs_list = Tarif.query.filter(Tarif.unlim_phone_internet == request_result['unlim_phone_internet'],
                                         Tarif.phone_minutes_quantity == request_result['phone_minutes_quantity'],
                                         Tarif.phone_sms_quantity == request_result['phone_sms_quantity']
                                         ).all()
        return tarifs_list
    elif condition4:
        print(4)
        tarifs_list = Tarif.query.filter(Tarif.unlim_phone_internet == request_result['unlim_phone_internet'],
                                         Tarif.unlim_phone_minutes == request_result['unlim_phone_minutes'],
                                         Tarif.phone_sms_quantity == request_result['phone_sms_quantity']
                                         ).all()
        return tarifs_list
    elif condition5:
        print(5)
        tarifs_list = Tarif.query.filter(Tarif.mobile_operator_name == request_result['mobile_operator_name'],
                                         Tarif.phone_internet_quantity == request_result['phone_internet_quantity'],
                                         Tarif.phone_minutes_quantity == request_result['phone_minutes_quantity'],
                                         Tarif.phone_sms_quantity == request_result['phone_sms_quantity']
                                         ).all()
        return tarifs_list
    elif condition6:
        print(6)
        tarifs_list = Tarif.query.filter(Tarif.mobile_operator_name == request_result['mobile_operator_name'],
                                         Tarif.phone_internet_quantity == request_result['phone_internet_quantity'],
                                         Tarif.unlim_phone_minutes == request_result['unlim_phone_minutes'],
                                         Tarif.phone_sms_quantity == request_result['phone_sms_quantity']
                                         ).all()
        return tarifs_list
    elif condition7:
        print(7)
        tarifs_list = Tarif.query.filter(Tarif.mobile_operator_name == request_result['mobile_operator_name'],
                                         Tarif.unlim_phone_internet == request_result['unlim_phone_internet'],
                                         Tarif.phone_minutes_quantity == request_result['phone_minutes_quantity'],
                                         Tarif.phone_sms_quantity == request_result['phone_sms_quantity']
                                         ).all()
        return tarifs_list
    elif condition8:
        print(8)
        tarifs_list = Tarif.query.filter(Tarif.mobile_operator_name == request_result['mobile_operator_name'],
                                         Tarif.unlim_phone_internet == request_result['unlim_phone_internet'],
                                         Tarif.unlim_phone_minutes == request_result['unlim_phone_minutes'],
                                         Tarif.phone_sms_quantity == request_result['phone_sms_quantity']
                                         ).all()
        return tarifs_list
