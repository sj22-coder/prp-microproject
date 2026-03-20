from flask import Blueprint, render_template, request, redirect
from database.db import get_db

expenses_bp = Blueprint('expenses', __name__)

@expenses_bp.route("/expenses", methods=["GET","POST"])
def expenses():

    db = get_db()

    if request.method == "POST":

        trip_id = request.form["trip_id"]
        amount = request.form["amount"]
        category = request.form["category"]

        db.execute(
        "INSERT INTO expenses(trip_id,amount,category) VALUES(?,?,?)",
        (trip_id,amount,category)
        )

        db.commit()

    data = db.execute("SELECT * FROM expenses").fetchall()

    trips = db.execute("SELECT * FROM trips").fetchall()

    return render_template("expenses.html", data=data, trips=trips) 
