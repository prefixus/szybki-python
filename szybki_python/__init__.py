"""Szybki Python — Zoptymalizowane i bezpieczne funkcje narzędziowe dla polskich projektów.

Zbudowane przy użyciu agentów AI (LangGraph + Qwen + Gemma Council + Security Auditor).
Licencja: MIT
"""

from .address import clean_polish_address, wyczysc_adres
from .dates import sformatuj_date_slownie, spell_polish_date
from .diacritics import strip_polish_diacritics, usun_diakrytyki
from .dowod import validate_id_card, waliduj_dowod
from .ean_bdo import waliduj_bdo, waliduj_ean13
from .gtu import extract_gtu_codes, wyciagnij_kody_gtu
from .gus import parse_gus_bir1_response, parsuj_odpowiedz_gus
from .iban import validate_iban_mod97, waliduj_iban
from .jpk import aggregate_jpk_sales, agreguj_jpk
from .krs import sanitize_krs_number, wyczysc_krs
from .ksef_xml import parse_ksef_xml_stream, parsuj_faktury_ksef
from .kwota_slownie import amount_in_words, kwota_slownie
from .names import classify_polish_name_gender, okresl_plec_imienia
from .nrb import route_nrb_bank, waliduj_nrb
from .payroll import calculate_polish_payroll_tax, oblicz_podatek_pit
from .phone import normalize_phone_number, normalizuj_telefon
from .plural import odmien_liczebnik, pluralize_polish
from .postal_codes import dopasuj_kod_pocztowy, route_postal_code
from .slugify import slugify_polish, stworz_slug
from .stemmer import obtnij_przyrostek, stem_polish_word
from .teryt import dopasuj_simc, route_teryt_simc
from .validators import batch_validate_pesel_nip, waliduj_nip, waliduj_pesel, waliduj_regon
from .vies import clean_vies_nip, wyczysc_nip_vies

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
    "okresl_plec_imienia",
    "classify_polish_name_gender",
    "wyczysc_krs",
    "sanitize_krs_number",
    "obtnij_przyrostek",
    "stem_polish_word",
    "parsuj_odpowiedz_gus",
    "parse_gus_bir1_response",
    "wyczysc_adres",
    "clean_polish_address",
    "oblicz_podatek_pit",
    "calculate_polish_payroll_tax",
    "sformatuj_date_slownie",
    "spell_polish_date",
    "waliduj_iban",
    "validate_iban_mod97",
    "wyciagnij_kody_gtu",
    "extract_gtu_codes",
]

__version__ = "0.3.0"
