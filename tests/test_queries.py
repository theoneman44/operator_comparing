# 'http://127.0.0.1:5000/?mobile_operator_name=0&phone_internet_quantity=30&phone_minutes_quantity=1000&phone_sms_quantity=250'

# import pytest
from flask import Flask
# from webapp.mobile.models import Links, Tarif, Tarif_3in1
# from webapp.mobile.queries import queries, queries_without_sms, standart_queries


def test__queries(client: Flask):
    # request = '/?mobile_operator_name=0&phone_internet_quantity=30&phone_minutes_quantity=1000&phone_sms_quantity=250'
    # queries(request) == 132
    pass
