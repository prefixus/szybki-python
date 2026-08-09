"""Unit tests for szybki_python open-source package."""

from szybki_python import (
    dopasuj_kod_pocztowy,
    parsuj_faktury_ksef,
    usun_diakrytyki,
    waliduj_nip,
    waliduj_pesel,
    waliduj_regon,
)


def test_usun_diakrytyki():
    text = "Zażółć gęślą jaźń ĄĆĘŁŃÓŚŹŻ"
    res = usun_diakrytyki(text, to_lower=True)
    assert res == "zazolc gesla jazn acelnoszz"

    res_case = usun_diakrytyki("Kraków", to_lower=False)
    assert res_case == "Krakow"


def test_dopasuj_kod_pocztowy():
    assert dopasuj_kod_pocztowy("00-001") == "Warszawa"
    assert dopasuj_kod_pocztowy("30-001") == "Kraków"
    assert dopasuj_kod_pocztowy("99-999") is None
    assert dopasuj_kod_pocztowy("invalid") is None


def test_parsuj_faktury_ksef():
    xml = """<Faktura><Podmiot1><NIP>1234567890</NIP></Podmiot1><FaWiersz><P_11>100.50</P_11></FaWiersz></Faktura>"""
    res = parsuj_faktury_ksef(xml)
    assert res["nip_list"] == ["1234567890"]
    assert res["total_netto"] == 100.50


def test_waliduj_pesel():
    assert waliduj_pesel("44051401359") is True
    assert waliduj_pesel("12345678900") is False
    assert waliduj_pesel("invalid") is False


def test_waliduj_nip():
    assert waliduj_nip("5260250995") is True
    assert waliduj_nip("526-025-09-95") is True
    assert waliduj_nip("0000000000") is False


def test_waliduj_regon():
    assert waliduj_regon("123456785") is True
    assert waliduj_regon("000000000") is False
