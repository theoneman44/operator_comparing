from webapp.mobile.models import Links, Tarif, Tarif_3in1


def test__model__links():
    link = Links(mobile_operator_name='МТС', tarif_name='НеТариф', page_link='https://moskva.mts.ru/personal/mobilnaya-svyaz/tarifi/vse-tarifi/mobile')
    assert link.__repr__() == 'Tarif МТС, НеТариф, https://moskva.mts.ru/personal/mobilnaya-svyaz/tarifi/vse-tarifi/mobile.'


def test__model__tarif():
    tarif = Tarif(mobile_operator_name='МТС', tarif_name='НеТариф', price=599)
    assert tarif.__repr__() == 'Tarif МТС, НеТариф, 599'


def test__model__tarif_3in1():
    tarif = Tarif_3in1(mobile_operator_name='Теле2', tarif_name='Black', price=800)
    assert tarif.__repr__() == 'Tarif Теле2, Black, 800'
