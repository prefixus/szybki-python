"""Szybki Python — Zoptymalizowane funkcje narzędziowe dla polskich projektów.

Zbudowane przy użyciu agentów AI (LangGraph + Qwen + Gemma Council).
Licencja: MIT
"""

from .diacritics import usun_diakrytyki, strip_polish_diacritics
from .postal_codes import dopasuj_kod_pocztowy, route_postal_code
from .ksef_xml import parsuj_faktury_ksef, parse_ksef_xml_stream
from .validators import waliduj_pesel, waliduj_nip, waliduj_regon, batch_validate_pesel_nip
from .kwota_slownie import kwota_slownie, amount_in_words
from .nrb import waliduj_nrb, route_nrb_bank
from .plural import odmien_liczebnik, pluralize_polish
from .ean_bdo import waliduj_ean13, waliduj_bdo

__all__ = [
    "usun_diakrytyki",
    "strip_polish_diacritics",
    "dopasuj_kod_pocztowy",
    "route_postal_code",
    "parsuj_faktury_ksef",
    "parse_ksef_xml_stream",
    "waliduj_pesel",
    "waliduj_nip",
    "waliduj_regon",
    "batch_validate_pesel_nip",
    "kwota_slownie",
    "amount_in_words",
    "waliduj_nrb",
    "route_nrb_bank",
    "odmien_liczebnik",
    "pluralize_polish",
    "waliduj_ean13",
    "waliduj_bdo",
]

__version__ = "0.2.0"
