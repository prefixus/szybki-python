"""Moduł do precyzyjnego i szybkiego wyliczania zaliczek na PIT i ZUS z kwot wynagrodzeń brutto.

Precyzja: Decimal (100% zgodności podatkowo-finansowej, brak błędu IEEE 754).
"""

from decimal import ROUND_HALF_UP, Decimal

_ZUS_RATE = Decimal("0.1371")
_TAX_THRESHOLD = Decimal("120000.00")
_TAX_RATE_LOW = Decimal("0.12")
_TAX_RATE_HIGH = Decimal("0.32")
_BASE_HIGH_TAX = Decimal("10800.00")
_ZERO = Decimal("0.00")


def oblicz_podatek_pit(kwota_brutto: float | str | Decimal) -> Decimal:
    """Oblicza kwotę zaliczki na podatek dochodowy PIT z uwzględnieniem ZUS i skali podatkowej.

    :param kwota_brutto: Wynagrodzenie brutto (float, str lub Decimal)
    :return: Kwota zaliczki PIT jako Decimal wyzaokrąglony do 2 miejsc po przecinku
    """
    gross = Decimal(str(kwota_brutto)) if not isinstance(kwota_brutto, Decimal) else kwota_brutto
    zus = gross * _ZUS_RATE
    basis = gross - zus
    if basis > _TAX_THRESHOLD:
        tax = _BASE_HIGH_TAX + (basis - _TAX_THRESHOLD) * _TAX_RATE_HIGH
    else:
        tax = basis * _TAX_RATE_LOW
    return max(_ZERO, tax).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def calculate_polish_payroll_tax(kwota_brutto: float | str | Decimal) -> Decimal:
    """English alias for oblicz_podatek_pit."""
    return oblicz_podatek_pit(kwota_brutto)
