 🌍 TripNest – Interactive Travel Bucket List & Expense Planner

🌟 Project Description

TripNest is a Flask-based web application designed to help users plan and organize their travel journeys. It allows users to create a personal bucket list of destinations, track visited places, and manage trip-related expenses in a simple and interactive way.

The application uses a structured backend with SQLite for data storage and provides a smooth user experience through dynamic templates and clean UI design.

🚀 Features
1. 🔐 User Registration & Login system
2. ✈️ Add and manage trips
3. 📍 Bucket List (Want to Visit places)
4. ✅ Mark trips as Visited
5. 💰 Expense tracking for each trip
6. 📊 Dashboard with travel statistics
7. 🧾 Organized database handling using SQLite

🛠️ Tech Stack
1. Backend: Python (Flask)
2. Frontend: HTML, CSS (Jinja2 Templates)
3. Database: SQLite
4. Version Control: Git & GitHub

📂 Project Structure

```
TripNest/
├── app.py
├── database/
│   └── db.py
├── modules/
│   ├── auth.py
│   ├── dashboard.py
│   ├── trips.py
│   ├── expenses.py
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_trip.html
│   ├── expenses.html
│   ├── want_to_go.html
│   ├── visited.html
├── static/
│   └── style.css
```

🗄️ Database Schema (SQLite)
1. Users Table:
id (Primary Key)
username (Unique)
password

2. Trips Table:
id (Primary Key)
place
budget
status (want / visited)

3. Expenses Table:
id (Primary Key)
trip_id (Foreign Key)
amount
category

⚙️ How to Run the Project
1. Clone the repository: git clone <your-repository-link>
2. Navigate to the project folder: cd TripNest
3. Install required dependencies: pip install flask
4. Run the application: python app.py
5. Open in browser: http://127.0.0.1:5000/

👉 The database will be automatically created when the app runs for the first time.

🔀 GitHub Collaboration
Followed feature branch strategy
Each module was developed separately
Pull Requests were used before merging into main
Regular commits made by all team members

Example branches:
feature-auth
feature-trips
feature-expenses
feature-dashboard
feature-ui

👥 Team Contributions:

Simran
1. Developed main application (app.py)
2. Implemented trips and expenses modules
3. Created add_trip and expenses templates

Heer
1. Built authentication system (login/register)
2. Handled user validation and database integration

Harsh
1. Designed dashboard UI and pages
2. Developed want_to_go and visited templates
3. Styled entire application using CSS

🎥 Demo Video

👉 Watch Project Demo

📌 Future Enhancements
1. 🔒 Password hashing for better security
2. 📍 Map integration for locations
3. 📱 Mobile responsive UI
4. 📊 Advanced analytics for expenses
5. ☁️ Migration to MongoDB or cloud database

⚠️ Notes
1. Ensure Python and Flask are installed
2. The project runs locally using SQLite
3. No external database setup required

💫 Final Thought: TripNest isn’t just a tracker—it’s a quiet companion for every place you dream of and every journey you complete.
