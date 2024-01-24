from webapp.mobile.models import Links, Tarif, Tarif_3in1


def test__model__links() -> bool:
    link = Links()
    link.mobile_operator_name = 'МТС'
    link.tarif_name = 'НеТариф'
    link.page_link = 'https://moskva.mts.ru/personal/mobilnaya-svyaz/tarifi/vse-tarifi/mobile'

    assert link.__repr__() == 'Tarif МТС, НеТариф, https://moskva.mts.ru/personal/mobilnaya-svyaz/tarifi/vse-tarifi/mobile.'


def test__model__tarif() -> bool:
    tarif = Tarif()
    tarif.mobile_operator_name = 'МТС'
    tarif.tarif_name = 'НеТариф'
    tarif.price = 599

    assert tarif.__repr__() == 'Tarif МТС, НеТариф, 599'


def test__model__tarif_3in1() -> bool:
    tarif = Tarif_3in1()
    tarif.mobile_operator_name = 'Теле2'
    tarif.tarif_name = 'Black'
    tarif.price = 800

    assert tarif.__repr__() == 'Tarif Теле2, Black, 800'
