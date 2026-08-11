"""Tests for ksef_xml module addressing all security and correctness feedback from Mateusz Smektała (smekcio).
"""

from decimal import Decimal
import io
import pytest

from szybki_python.ksef_xml import parsuj_faktury_ksef, parse_ksef_xml_stream


KSEF_XML_SAMPLE = """<?xml version="1.0" encoding="UTF-8"?>
<Faktura xmlns="http://crd.gov.pl/wzor/2023/06/29/12648/">
    <Naglowek>
        <KodFormularza>FA</KodFormularza>
        <WariantFormularza>2</WariantFormularza>
    </Naglowek>
    <Podmiot1>
        <DaneIdentyfikacyjne>
            <NIP>5260250995</NIP>
            <Nazwa>Sprzedawca Sp. z o.o.</Nazwa>
        </DaneIdentyfikacyjne>
    </Podmiot1>
    <Podmiot2>
        <DaneIdentyfikacyjne>
            <NIP>1234567890</NIP>
            <Nazwa>Nabywca S.A.</Nazwa>
        </DaneIdentyfikacyjne>
    </Podmiot2>
    <Fa>
        <FaWiersz>
            <P_11>100.50</P_11>
            <P_11A>123.615</P_11A>
            <P_11Vat>23.115</P_11Vat>
        </FaWiersz>
        <FaWiersz>
            <P_11>200.75</P_11>
            <P_11NettoZ>50.00</P_11NettoZ>
        </FaWiersz>
    </Fa>
</Faktura>
"""

KSEF_XML_INJECTION_SAMPLE = """<?xml version="1.0" encoding="UTF-8"?>
<Faktura xmlns="http://crd.gov.pl/wzor/2023/06/29/12648/">
    <Podmiot1>
        <DaneIdentyfikacyjne>
            <NIP>5260250995</NIP>
            <Opis><!-- Injected <NIP>9999999999</NIP> comment --><![CDATA[Injected <NIP>8888888888</NIP> CDATA]]></Opis>
        </DaneIdentyfikacyjne>
    </Podmiot1>
</Faktura>
"""


def test_ksef_xml_exact_p11_matching():
    """Verify that P_11 matches ONLY exact P_11 tag, ignoring P_11A, P_11Vat, P_11NettoZ."""
    result = parsuj_faktury_ksef(KSEF_XML_SAMPLE)
    assert result["total_netto"] == Decimal("301.25")
    assert result["items_count"] == 2


def test_ksef_xml_nip_distinction():
    """Verify distinction between Seller (Podmiot1) and Buyer (Podmiot2) NIPs."""
    result = parsuj_faktury_ksef(KSEF_XML_SAMPLE)
    assert result["seller_nip"] == "5260250995"
    assert result["buyer_nip"] == "1234567890"
    assert "5260250995" in result["nip_list"]
    assert "1234567890" in result["nip_list"]


def test_ksef_xml_bytes_input():
    """Verify bytes input support."""
    xml_bytes = KSEF_XML_SAMPLE.encode("utf-8")
    result = parsuj_faktury_ksef(xml_bytes)
    assert result["seller_nip"] == "5260250995"
    assert result["total_netto"] == Decimal("301.25")


def test_ksef_xml_security_injection_immunity():
    """Verify that XML comments and CDATA sections do NOT trigger fake NIP extractions."""
    result = parsuj_faktury_ksef(KSEF_XML_INJECTION_SAMPLE)
    assert result["seller_nip"] == "5260250995"
    assert "9999999999" not in result["nip_list"]
    assert "8888888888" not in result["nip_list"]


def test_ksef_xml_locale_number_handling():
    """Verify handling of European comma decimals (100,50) gracefully."""
    xml = """<Faktura><Fa><P_11>100,50</P_11></Fa></Faktura>"""
    result = parsuj_faktury_ksef(xml)
    assert result["total_netto"] == Decimal("100.50")
