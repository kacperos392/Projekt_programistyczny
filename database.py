import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS samochody (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marka TEXT NOT NULL,
    model TEXT NOT NULL,
    cena REAL NOT NULL CHECK(cena >= 0),
    vin TEXT,
    sprzedawca TEXT,
    pojemnosc_silnika REAL,
    moc INTEGER,
    rocznik INTEGER,
    skrzynia_biegow TEXT,
    przebieg INTEGER CHECK(przebieg IS NULL OR przebieg >= 0),
    stan_techniczny TEXT,
    lokalizacja TEXT,
    paliwo TEXT,
    data_dodania TEXT DEFAULT CURRENT_TIMESTAMP
);
"""

def get_connection(database_path):
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def init_db(database_path):
    Path(database_path).parent.mkdir(parents=True, exist_ok=True)
    with get_connection(database_path) as connection:
        connection.executescript(SCHEMA)
