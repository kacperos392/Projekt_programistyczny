<<<<<<< HEAD
# Analiza cen samochodów używanych

Prosty szkielet aplikacji internetowej w Pythonie: Flask + SQLite + HTML/CSS.

## Wymagania
- Python 3.10 lub nowszy
- pip

## Uruchomienie – Windows

```bash
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Uruchomienie – Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Otwórz w przeglądarce: http://127.0.0.1:5000

Baza `cars.db` utworzy się automatycznie przy pierwszym uruchomieniu.

## Testy

```bash
pytest
```

## Struktura i podział pracy

1. **Osoba 1 – baza danych:** `database.py`, schemat tabeli, walidacja i przykładowe dane.
2. **Osoba 2 – backend:** `app.py`, `routes/cars.py`, formularze i wyszukiwanie.
3. **Osoba 3 – analiza:** `analytics/analysis.py`, dodatkowe statystyki i później Pandas.
4. **Osoba 4 – interfejs:** `templates/`, `static/style.css`, wygląd i wygoda obsługi.
5. **Osoba 5 – wykresy/testy/dokumentacja:** `routes/analysis.py`, `tests/`, README; w kolejnym etapie wykresy Matplotlib.

## Zasady współpracy

- Ustalcie zmiany w strukturze bazy wspólnie, zanim ktoś zmieni nazwy kolumn.
- Każda osoba pracuje na osobnej gałęzi Git, np. `feature/database`.
- Przed połączeniem zmian uruchomcie aplikację i testy.
- Nie commitujcie `venv/` ani pliku `cars.db`.

## Ważne
To jest szkielet edukacyjny, a nie gotowy system produkcyjny. Przed użyciem publicznym trzeba dodać m.in. silniejszą walidację wszystkich pól, konfigurację sekretów, obsługę błędów i ochronę formularzy. Dane w bazie powinny być prawdziwe albo wyraźnie oznaczone jako testowe.
=======
# Projekt_programistyczny
>>>>>>> 5c2abe6206b7fe1450a6f4779055e3184be1d936
