"""Unit tests for phone, vies, and jpk modules in packages/szybki_python."""

from decimal import Decimal

from szybki_python.jpk import agreguj_jpk
from szybki_python.phone import normalizuj_telefon
from szybki_python.vies import wyczysc_nip_vies


def test_normalizuj_telefon():
    assert normalizuj_telefon("+48 500 100 200") == "+48500100200"
    assert normalizuj_telefon("500-100-200") == "+48500100200"
    assert normalizuj_telefon("invalid") is None


def test_wyczysc_nip_vies():
    assert wyczysc_nip_vies("PL 526-025-09-95") == "5260250995"
    assert wyczysc_nip_vies("5260250995") == "5260250995"
    assert wyczysc_nip_vies("INVALID") is None


def test_agreguj_jpk():
    xml = "<JPK><SprzedazWiersz><K_19>1000.50</K_19><K_19>500,25</K_19></SprzedazWiersz></JPK>"
    total = agreguj_jpk(xml, target_tag="K_19")
    assert total == Decimal("1500.75")
