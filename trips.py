from flask import Blueprint, render_template, request, redirect
from database.db import get_db

trips_bp = Blueprint('trips', __name__)

@trips_bp.route("/add_trip", methods=["GET","POST"])
def add_trip():

    if request.method == "POST":

        place = request.form["place"]
        budget = request.form["budget"]

        db = get_db()

        db.execute(
        "INSERT INTO trips(place,budget,status) VALUES(?,?,?)",
        (place,budget,"want"))

        db.commit()

        return redirect("/dashboard")

    return render_template("add_trip.html")


@trips_bp.route("/want_to_go")
def want():

    db = get_db()

    trips = db.execute(
    "SELECT * FROM trips WHERE status='want'"
    ).fetchall()

    return render_template("want_to_go.html", trips=trips)


@trips_bp.route("/visited/<int:id>")
def mark_visited(id):

    db = get_db()

    db.execute(
    "UPDATE trips SET status='visited' WHERE id=?",
    (id,)
    )

    db.commit()

    return redirect("/dashboard")


@trips_bp.route("/visited")
def visited():

    db = get_db()

    trips = db.execute(
    "SELECT * FROM trips WHERE status='visited'"
    ).fetchall()

    return render_template("visited.html", trips=trips)
@trips_bp.route("/delete_trip/<int:id>")
def delete_trip(id):

    db = get_db()

    db.execute("DELETE FROM trips WHERE id=?", (id,))

    db.commit()

    return redirect("/dashboard")