 🌍 TripNest – Interactive Travel Bucket List & Expense Planner

🌟 Project Description

TripNest is a Flask-based web application designed to help users plan and organize their travel journeys. It allows users to create a personal bucket list of destinations, track visited places, and manage trip-related expenses in a simple and interactive way.

The application uses a structured backend with SQLite for data storage and provides a smooth user experience through dynamic templates and clean UI design.

🚀 Features
🔐 User Registration & Login system
✈️ Add and manage trips
📍 Bucket List (Want to Visit places)
✅ Mark trips as Visited
💰 Expense tracking for each trip
📊 Dashboard with travel statistics
🧾 Organized database handling using SQLite

🛠️ Tech Stack
Backend: Python (Flask)
Frontend: HTML, CSS (Jinja2 Templates)
Database: SQLite
Version Control: Git & GitHub

📂 Project Structure
TripNest/
│── app.py
│── database/
│   └── db.py
│── modules/
│   ├── auth.py
│   ├── dashboard.py
│   ├── trips.py
│   ├── expenses.py
│── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_trip.html
│   ├── expenses.html
│   ├── want_to_go.html
│   ├── visited.html
│── static/
│   └── style.css

🗄️ Database Schema (SQLite)
Users Table
id (Primary Key)
username (Unique)
password
Trips Table
id (Primary Key)
place
budget
status (want / visited)
Expenses Table
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

👥 Team Contributions

Simran

Developed main application (app.py)
Implemented trips and expenses modules
Created add_trip and expenses templates

Heer

Built authentication system (login/register)
Handled user validation and database integration

Harsh

Designed dashboard UI and pages
Developed want_to_go and visited templates
Styled entire application using CSS

🎥 Demo Video

👉 Watch Project Demo

📌 Future Enhancements
🔒 Password hashing for better security
📍 Map integration for locations
📱 Mobile responsive UI
📊 Advanced analytics for expenses
☁️ Migration to MongoDB or cloud database
⚠️ Notes
Ensure Python and Flask are installed
The project runs locally using SQLite
No external database setup required

💫 Final Thought

TripNest isn’t just a tracker—it’s a quiet companion for every place you dream of and every journey you complete.
