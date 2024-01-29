# 'http://127.0.0.1:5000/?mobile_operator_name=0&phone_internet_quantity=30&phone_minutes_quantity=1000&phone_sms_quantity=250'
# ImmutableMultiDict([('mobile_operator_name', '0'), ('phone_internet_quantity', '20'), ('phone_minutes_quantity', '400'), ('phone_sms_quantity', '100')])

def test__queries(query) -> None:
    # assert query.response == 'Tarif МТС, НЕТАРИФ, 655'
    assert query.status == '200 OK'
    # assert query.request == 'Tarif МТС, НЕТАРИФ, 655'
