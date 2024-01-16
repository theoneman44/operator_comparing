from sqlalchemy import between
from typing import Any
from webapp.all_in.models import Tarif_3in1

# mobile_operator_name=0&phone_internet_qty=0&phone_minutes_qty=0&internet_speed=0&family_num=0


def queries(request_result: Any) -> Tarif_3in1:
    tarifs_list = Tarif_3in1.query
    tarifs_list = phone_minutes_filter(request_result, tarifs_list)
    tarifs_list = channels_qty_filter(request_result, tarifs_list)
    tarifs_list = standart_queries(request_result, tarifs_list)

    # если тарифы не нашлись исключаем из поиска фильтр по каналам и показываем результат
    if len(tarifs_list) == 0:
        tarifs_list = Tarif_3in1.query
        tarifs_list = phone_minutes_filter(request_result, tarifs_list)
        tarifs_list = standart_queries(request_result, tarifs_list)
        # если тарифы не нашлись исключаем из поиска фильтр по каналам и минутам в пакете и показываем результат
        if len(tarifs_list) == 0:
            tarifs_list = Tarif_3in1.query
            tarifs_list = standart_queries(request_result, tarifs_list)
            return tarifs_list
        else:
            return tarifs_list
    else:
        return tarifs_list


def phone_minutes_filter(request_result: Any, tarifs_list: Tarif_3in1) -> Tarif_3in1:
    tarifs_list = tarifs_list.filter(between(Tarif_3in1.phone_minutes_qty, int(request_result['phone_minutes_qty']) - 301,
                                     int(request_result['phone_minutes_qty']) + 301)
                                     )
    return tarifs_list


def channels_qty_filter(request_result: Any, tarifs_list: Tarif_3in1) -> Tarif_3in1:
    tarifs_list = tarifs_list.filter(between(Tarif_3in1.channels_qty, int(request_result['channels_qty']) - 101,
                                     int(request_result['channels_qty']) + 101)
                                     )
    return tarifs_list


def standart_queries(request_result: Any, tarifs_list: Tarif_3in1) -> Tarif_3in1:
    tarifs_list = tarifs_list.filter(between(Tarif_3in1.phone_internet_qty, int(request_result['phone_internet_qty']) - 11,
                                     int(request_result['phone_internet_qty']) + 11),
                                     between(Tarif_3in1.internet_speed, int(request_result['internet_speed']) - 301,
                                     int(request_result['internet_speed']) + 301)
                                     )

    if request_result['mobile_operator_name'] != '0':
        tarifs_list = tarifs_list.filter(Tarif_3in1.mobile_operator_name == request_result['mobile_operator_name'])

    tarifs_list = tarifs_list.order_by(Tarif_3in1.price.asc()).all()
    return tarifs_list
