from flask import Flask
from modules.auth import auth_bp
from modules.trips import trips_bp
from modules.expenses import expenses_bp
from modules.dashboard import dashboard_bp
from database.db import init_db

app = Flask(__name__)
app.secret_key = "tripnest_secret"

init_db()

app.register_blueprint(auth_bp)
app.register_blueprint(trips_bp)
app.register_blueprint(expenses_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(debug=True)