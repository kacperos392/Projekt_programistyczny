from flask import Blueprint, current_app, render_template
from database import get_connection
from analytics.analysis import get_summary, get_average_by_brand

analysis_bp = Blueprint("analysis", __name__, url_prefix="/analiza")

@analysis_bp.get("/")
def dashboard():
    with get_connection(current_app.config["DATABASE"]) as connection:
        summary = get_summary(connection)
        by_brand = get_average_by_brand(connection)
    return render_template("analysis.html", summary=summary, by_brand=by_brand)
