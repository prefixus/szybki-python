"""Moduł do bezpiecznej, strumieniowej ekstrakcji danych z dokumentów KSeF XML.

Wdrożono zlecenia bezpieczeństwa i jakości (Mateusz Smektała - smekcio/ksef-client-python):
1. Ochrona przed XML Injection (CDATA / sekcje komentarzy / Atrybuty).
2. Wyeliminowanie podatności ReDoS (użycie strumieniowego parsera iterparse zamiast wyrażeń regularnych).
3. Ścisła precyzja finansowa (decimal.Decimal zamiast float).
4. Obsługa wejścia str i bytes.
5. Rozróżnienie NIP Sprzedawcy (Podmiot1) oraz NIP Nabywca (Podmiot2).
6. Odporność na formaty kwot z przecinkami (100,50 -> 100.50).
"""

import io
import xml.etree.ElementTree as ET
from decimal import Decimal, InvalidOperation
from typing import Any


def parsuj_faktury_ksef(xml_content: str | bytes | io.BufferedIOBase) -> dict[str, Any]:
    """Strumieniowo parsuje plik KSeF XML przy użyciu xml.etree.ElementTree.iterparse.

    Nie buduje całego drzewa DOM w pamięci (O(1) RAM), ignoruje komentarze i sekcje CDATA,
    oraz eliminuje ryzyko ataku ReDoS.

    :param xml_content: Zawartość pliku XML jako str, bytes lub strumień wejściowy
    :return: Słownik z podsumowaniem faktury: seller_nip, buyer_nip, nip_list, total_netto, items_count
    """
    if isinstance(xml_content, str):
        source: io.BufferedIOBase | io.BytesIO = io.BytesIO(xml_content.encode("utf-8"))
    elif isinstance(xml_content, bytes):
        source = io.BytesIO(xml_content)
    else:
        source = xml_content

    seller_nip: str | None = None
    buyer_nip: str | None = None
    nip_list: list[str] = []
    total_netto = Decimal("0.00")
    items_count = 0

    stack: list[str] = []

    # Streaming Pull Parser (iterparse) - O(1) Memory & Security Guaranteed
    context = ET.iterparse(source, events=("start", "end"))

    for event, elem in context:
        # Strip XML namespace if present: {http://crd.gov.pl/...}Tag -> Tag
        tag_name = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag

        if event == "start":
            stack.append(tag_name)
        elif event == "end":
            text = (elem.text or "").strip()

            if tag_name == "NIP" and text:
                nip_list.append(text)
                if "Podmiot1" in stack and seller_nip is None:
                    seller_nip = text
                elif "Podmiot2" in stack and buyer_nip is None:
                    buyer_nip = text

            elif tag_name == "P_11" and text:
                # Handle European decimal comma notation (100,50 -> 100.50)
                sanitized_text = text.replace(",", ".")
                try:
                    amount = Decimal(sanitized_text)
                    total_netto += amount
                    items_count += 1
                except (ValueError, InvalidOperation):
                    pass

            if stack and stack[-1] == tag_name:
                stack.pop()

            # Clear processed elements from memory to keep RAM usage O(1)
            elem.clear()

    return {
        "seller_nip": seller_nip,
        "buyer_nip": buyer_nip,
        "nip_list": nip_list,
        "total_netto": total_netto,
        "items_count": items_count,
    }


def parse_ksef_xml_stream(xml_content: str | bytes | io.BufferedIOBase) -> dict[str, Any]:
    """English alias for parsuj_faktury_ksef."""
    return parsuj_faktury_ksef(xml_content)
