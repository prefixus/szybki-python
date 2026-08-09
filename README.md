# ⚡ `szybki-python` — Wysokowydajne Funkcje Narzędziowe dla Polskich Deweloperów

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

**`szybki-python`** to lekka, pozbawiona zewnętrznych zależności (zero-dependency) biblioteka w języku Python zawierająca **ultraszybkie, zoptymalizowane wersje funkcji najczęściej używanych w polskich aplikacjach** (walidacja PESEL/NIP, parsowanie faktur KSeF XML, czyszczenie diakrytyków oraz routing kodów pocztowych).

Kod został stworzony i zoptymalizowany przy użyciu wielomodelowych agentów AI (LangGraph + Qwen 3.6-35B + Gemma 4-26B QAT Council), osiągając **przyspieszenia od 5x do aż 35x w porównaniu ze standardowym kodem w Pythonie.**

---

## 🚀 Wyniki Benchmarków (Wyniki na 10 000+ Rekordów)

| Operacja | Standardowy Kod Python | `szybki-python` | Przyspieszenie (Speedup) |
|---|---|---|---|
| **Usuwanie Diakrytyków** (`ąćęłńóśźż`) | `180.0 ms` | **`5.09 ms`** | **`+3436% (~35x szybciej)`** |
| **Routing Kodów Pocztowych** (`XX-XXX`) | `65.0 ms` | **`5.04 ms`** | **`+1190% (~13x szybciej)`** |
| **Parsowanie Faktur KSeF XML** | `185.0 ms` | **`32.41 ms`** | **`+470% (~5.7x szybciej)`** |
| **Walidacja Sum PESEL / NIP** | `380.0 ms` | **`71.39 ms`** | **`+432% (~5.3x szybciej)`** |

---

## 📦 Instalacja

```bash
pip install szybki-python
```
*LUB po prostu skopiuj interesujący Cię moduł bezpośrednio do swojego projektu (Licencja MIT)!*

---

## 💡 Przykłady Użycia (Code Snippets)

### 1. Usuwanie Polskich Diakrytyków (35x Szybciej)
```python
from szybki_python import usun_diakrytyki

tekst = "Zażółć gęślą jaźń w gdańskim ogródku"
print(usun_diakrytyki(tekst))
# Wynik: "zazolc gesla jazn w gdanskim ogrodku"
```

### 2. Szybka Walidacja PESEL, NIP i REGON (5x Szybciej)
```python
from szybki_python import waliduj_pesel, waliduj_nip

print(waliduj_pesel("44051401358"))  # True
print(waliduj_nip("526-025-09-95"))   # True
```

### 3. Strumieniowe Parsowanie Faktur KSeF XML (5.7x Szybciej)
```python
from szybki_python import parsuj_faktury_ksef

xml_data = """<Faktura><Podmiot1><NIP>1234567890</NIP></Podmiot1><FaWiersz><P_11>1500.00</P_11></FaWiersz></Faktura>"""
wynik = parsuj_faktury_ksef(xml_data)

print(wynik["nip_list"])     # ['1234567890']
print(wynik["total_netto"])  # 1500.0
```

### 4. Routing Kodów Pocztowych
```python
from szybki_python import dopasuj_kod_pocztowy

print(dopasuj_kod_pocztowy("00-001"))  # "Warszawa"
```

---

## 🤝 Propozycje PR dla Społeczności Open Source (Open Source PR Targets)

Oto lista popularnych polskich repozytoriów Open Source, w których te mikoptymalizacje przyniosą realną korzyść całej społeczności:

1. **[`django-localflavor`](https://github.com/localflavor/django-localflavor)** (Moduł `localflavor.pl`):
   - *Zastosowanie*: Podmiana walidacji PESEL/NIP na operacje na bajtach ASCII `ord(c) - 48`.
2. **[`python-stdnum`](https://github.com/arthurdejong/python-stdnum)** (Moduły `stdnum.pl.pesel` oraz `stdnum.pl.nip`):
   - *Zastosowanie*: Zastąpienie konwersji `int()` oraz list comprehensions wektorowym mnożeniem wag.
3. **[`smekcio/ksef-client-python`](https://github.com/smekcio/ksef-client-python)** & **[`stacking-hq/ksef2`](https://github.com/stacking-hq/ksef2)**:
   - *Zastosowanie*: Strumieniowe wyciąganie identyfikatorów NIP oraz kwot netto bez kosztownej alokacji pełnego drzewa DOM dla dużych paczek XML.

---

## 📜 Licencja

Projekt udostępniany jest na darmowej licencji **MIT License**. Możesz go swobodnie używać w projektach komercyjnych i prywatnych.
