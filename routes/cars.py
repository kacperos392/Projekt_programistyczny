from flask import Blueprint, current_app, render_template, request, redirect, url_for, flash
from database import get_connection

cars_bp = Blueprint("cars", __name__)

FIELDS = [
    "marka", "model", "cena", "vin", "sprzedawca",
    "pojemnosc_silnika", "moc", "rocznik", "skrzynia_biegow",
    "przebieg", "stan_techniczny", "lokalizacja", "paliwo"
]

def db():
    return get_connection(current_app.config["DATABASE"])

@cars_bp.route("/samochody", methods=["GET", "POST"])
def list_cars():
    if request.method == "POST":
        form = request.form
        try:
            marka = form.get("marka", "").strip()
            model = form.get("model", "").strip()
            cena = float(form.get("cena", ""))
            if not marka or not model or cena < 0:
                raise ValueError
        except ValueError:
            flash("Podaj poprawną markę, model i nieujemną cenę.", "error")
            return redirect(url_for("cars.list_cars"))

        values = []
        for field in FIELDS:
            value = form.get(field, "").strip() or None
            if field == "cena":
                value = cena
            elif field in ("rocznik", "moc", "przebieg"):
                value = int(value) if value else None
            elif field == "pojemnosc_silnika":
                value = float(value) if value else None
            values.append(value)

        placeholders = ", ".join("?" for _ in FIELDS)
        with db() as connection:
            connection.execute(
                f"INSERT INTO samochody ({', '.join(FIELDS)}) VALUES ({placeholders})",
                values
            )
        flash("Samochód został dodany.", "success")
        return redirect(url_for("cars.list_cars"))

    marka = request.args.get("marka", "").strip()
    query = "SELECT * FROM samochody WHERE 1=1"
    params = []
    if marka:
        query += " AND marka LIKE ?"
        params.append(f"%{marka}%")
    query += " ORDER BY data_dodania DESC, id DESC"

    with db() as connection:
        cars = connection.execute(query, params).fetchall()
    return render_template("cars.html", samochody=cars, selected_marka=marka)
