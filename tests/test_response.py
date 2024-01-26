import pytest
from flask import Flask


@pytest.mark.parametrize('url',
                         [('/images/megafon_banner.jpg'),
                          ('/images/mts_banner.jpg'),
                          ('/'),
                          ('/all_in'),
                          ('/?mobile_operator_name=МТС&phone_internet_quantity=30&phone_minutes_quantity=1000&phone_sms_quantity=250'),
                          ('/all_in?mobile_operator_name=0&phone_internet_qty=30&phone_minutes_qty=1000&internet_speed=400&channels_qty=200')
                          ])
def test__status_codes(client: Flask, url: str):
    response = client.get(url)
    assert response.status_code == 200
