from flask import Blueprint, render_template, request, redirect
import re
from database.db import get_db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        db = get_db()

        user = db.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username,password)).fetchone()

        if user:
            return redirect("/dashboard")

    return render_template("login.html")


@auth_bp.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if not re.match("^[A-Za-z0-9]{4,}$", username):
            return "Invalid Username"

        db = get_db()

        db.execute(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (username,password))

        db.commit()

        return redirect("/")

    return render_template("register.html")