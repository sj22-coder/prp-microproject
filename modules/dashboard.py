from flask import Blueprint, render_template
from database.db import get_db
import statistics

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route("/dashboard")
def dashboard():

    db = get_db()

    trips = db.execute("SELECT * FROM trips").fetchall()

    budgets = [trip["budget"] for trip in trips]

    avg_budget = 0

    if budgets:
        avg_budget = statistics.mean(budgets)

    total = len(trips)

    visited = len([t for t in trips if t["status"]=="visited"])

    return render_template(
        "dashboard.html",
        trips=trips,
        avg_budget=avg_budget,
        total=total,
        visited=visited
    )
