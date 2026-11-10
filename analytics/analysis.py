def get_summary(connection):
    row = connection.execute("""
        SELECT COUNT(*) AS liczba,
               AVG(cena) AS srednia,
               MIN(cena) AS minimum,
               MAX(cena) AS maksimum
        FROM samochody
    """).fetchone()
    return dict(row)

def get_average_by_brand(connection):
    rows = connection.execute("""
        SELECT marka, COUNT(*) AS liczba, AVG(cena) AS srednia_cena
        FROM samochody
        GROUP BY marka
        ORDER BY srednia_cena DESC
    """).fetchall()
    return [dict(row) for row in rows]
