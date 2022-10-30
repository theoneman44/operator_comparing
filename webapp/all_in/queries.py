from sqlalchemy import between

from webapp.all_in.models import Tarif_3in1

# mobile_operator_name=0&phone_internet_qty=0&phone_minutes_qty=0&internet_speed=0&family_num=0


def queries(request_result):

    tarifs_list = Tarif_3in1.query.filter(between(Tarif_3in1.phone_internet_qty, int(request_result['phone_internet_qty']) - 5,
                                          int(request_result['phone_internet_qty']) + 5),
                                          between(Tarif_3in1.phone_minutes_qty, int(request_result['phone_minutes_qty']) - 199,
                                          int(request_result['phone_minutes_qty']) + 199),
                                          between(Tarif_3in1.internet_speed, int(request_result['internet_speed']) - 100,
                                          int(request_result['internet_speed']) + 100),
                                          between(Tarif_3in1.channels_qty, int(request_result['channels_qty']) - 50,
                                          int(request_result['channels_qty']) + 50)
                                          )

    # if request_result['family_num'] > '0':
    #     tarifs_list = tarifs_list.filter(Tarif_3in1.family_num > '0')

    if request_result['mobile_operator_name'] != '0':
        tarifs_list = tarifs_list.filter(Tarif_3in1.mobile_operator_name == request_result['mobile_operator_name'])

    tarifs_list = tarifs_list.order_by(Tarif_3in1.price.asc()).all()

    return tarifs_list
