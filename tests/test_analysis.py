import sqlite3
from analytics.analysis import get_summary, get_average_by_brand

def test_summary_and_brand_average():
    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row
    connection.execute("""
        CREATE TABLE samochody (
            id INTEGER PRIMARY KEY, marka TEXT, cena REAL
        )
    """)
    connection.executemany(
        "INSERT INTO samochody (marka, cena) VALUES (?, ?)",
        [("Toyota", 50000), ("Toyota", 70000), ("BMW", 90000)]
    )
    summary = get_summary(connection)
    assert summary["liczba"] == 3
    assert summary["srednia"] == 70000
    brands = get_average_by_brand(connection)
    assert brands[0]["marka"] == "BMW"
    connection.close()
