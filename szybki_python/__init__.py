"""Szybki Python — Zoptymalizowane i bezpieczne funkcje narzędziowe dla polskich projektów.

Zbudowane przy użyciu agentów AI (LangGraph + Qwen + Gemma Council + Security Auditor).
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
from .slugify import stworz_slug, slugify_polish
from .dowod import waliduj_dowod, validate_id_card
from .teryt import dopasuj_simc, route_teryt_simc
from .phone import normalizuj_telefon, normalize_phone_number
from .vies import wyczysc_nip_vies, clean_vies_nip
from .jpk import agreguj_jpk, aggregate_jpk_sales

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
    "stworz_slug",
    "slugify_polish",
    "waliduj_dowod",
    "validate_id_card",
    "dopasuj_simc",
    "route_teryt_simc",
    "normalizuj_telefon",
    "normalize_phone_number",
    "wyczysc_nip_vies",
    "clean_vies_nip",
    "agreguj_jpk",
    "aggregate_jpk_sales",
]

__version__ = "0.3.0"
