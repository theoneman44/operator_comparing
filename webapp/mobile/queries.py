from sqlalchemy import between
from typing import Any

from webapp.mobile.models import Tarif

# mobile_operator_name=0&phone_internet_quantity=0&unlim_phone_internet=0&phone_minutes_quantity=0&unlim_phone_minutes=0&phone_sms_quantity=0&
# social_offer_price=0&messenger_price=0&music_offer_price=0&video_offer_price=0&stream_offer_price=0


def queries(request_result: Any) -> Any:

    tarifs_list = Tarif.query.filter(between(Tarif.phone_sms_quantity, int(request_result['phone_sms_quantity']) - 50,
                                             int(request_result['phone_sms_quantity']) + 50
                                             ))

    tarifs_list = standart_queries(request_result, tarifs_list)

    # если тарифы не нашлись исключаем из поиска смс фильтр и показываем результат
    if len(tarifs_list) == 0:
        tarifs_list = queries_without_sms(request_result)
        return tarifs_list
    else:
        print(f'Тарифы {tarifs_list}, тип {type(tarifs_list)}')
        return tarifs_list


def standart_queries(request_result: Any, tarifs_list: Tarif) -> Tarif:
    if request_result['mobile_operator_name'] != '0':
        tarifs_list = tarifs_list.filter(Tarif.mobile_operator_name == request_result['mobile_operator_name'])

    if 'unlim_phone_internet' not in request_result.keys():
        tarifs_list = tarifs_list.filter(between(Tarif.phone_internet_quantity, int(request_result['phone_internet_quantity']) - 5,
                                                 int(request_result['phone_internet_quantity']) + 5
                                                 ))
    elif request_result['unlim_phone_internet'] == '1':
        tarifs_list = tarifs_list.filter(Tarif.unlim_phone_internet == request_result['unlim_phone_internet'])

    if 'unlim_phone_minutes' not in request_result.keys():
        tarifs_list = tarifs_list.filter(between(Tarif.phone_minutes_quantity, int(request_result['phone_minutes_quantity']) - 199,
                                                 int(request_result['phone_minutes_quantity']) + 199
                                                 ))
    elif request_result['unlim_phone_minutes'] == '1':
        tarifs_list = tarifs_list.filter(Tarif.unlim_phone_minutes == request_result['unlim_phone_minutes'])

    tarifs_list = tarifs_list.order_by(Tarif.price.asc()).all()
    return tarifs_list


def queries_without_sms(request_result: Any) -> Tarif:
    tarifs_list = Tarif.query
    tarifs_list = standart_queries(request_result, tarifs_list)
    return tarifs_list
