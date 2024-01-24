import pytest
from flask import Flask


@pytest.mark.parametrize('url, response_code',
                         [('/images/megafon_banner.jpg', 200),
                          ('/images/mts_banner.jpg', 200),
                          ('/', 200),
                          ('/all_in', 200),
                          ('/?mobile_operator_name=МТС&phone_internet_quantity=30&phone_minutes_quantity=1000&phone_sms_quantity=250', 200),
                          ('/all_in?mobile_operator_name=0&phone_internet_qty=30&phone_minutes_qty=1000&internet_speed=400&channels_qty=200', 200)
                          ])
def test__status_codes(client: Flask, url: str, response_code: int) -> bool:
    response = client.get(url)
    assert response.status_code == response_code
