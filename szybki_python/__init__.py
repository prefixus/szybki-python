"""Szybki Python — Zoptymalizowane funkcje narzędziowe dla polskich projektów.

Zbudowane przy użyciu agentów AI (LangGraph + Qwen + Gemma Council).
Licencja: MIT
"""

from .diacritics import strip_polish_diacritics, usun_diakrytyki
from .ean_bdo import waliduj_bdo, waliduj_ean13
from .ksef_xml import parse_ksef_xml_stream, parsuj_faktury_ksef
from .kwota_slownie import amount_in_words, kwota_slownie
from .nrb import route_nrb_bank, waliduj_nrb
from .plural import odmien_liczebnik, pluralize_polish
from .postal_codes import dopasuj_kod_pocztowy, route_postal_code
from .validators import batch_validate_pesel_nip, waliduj_nip, waliduj_pesel, waliduj_regon

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
