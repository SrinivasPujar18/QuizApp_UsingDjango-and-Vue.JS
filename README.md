# QuizApp_UsingDjango-and-Vue.JS
This Quiz App is built using Django (backend) and Vue.js (frontend). The Django backend manages APIs, question data, and category-based quiz logic. Users start on the home page, where they select a quiz category. On clicking Submit, Vue.js redirects them to the quiz page with that category.

---
# 🎯 Quiz App using Django and Vue.js

A full-stack *Quiz Application* built with *Django (Backend)* and *Vue.js (Frontend)*.  
This project allows users to take quizzes, view scores, and manage questions through an interactive web interface.
---

## 🚀 Features
-  Create and take quizzes dynamically  
-  User authentication (login & signup)  
-  View quiz results and performance  
-  Django REST Framework-based API  
-  Interactive frontend built with Vue.js  
-  Data stored securely using Django ORM and SQLite/PostgreSQL  
---

## 🧩 Tech Stack
| Layer | Technology |
|-------|-------------|
| Frontend | Vue.js, HTML, CSS, JavaScript |
| Backend | Django, Django REST Framework |
| Database | SQLite (default) / PostgreSQL |
| Version Control | Git & GitHub |
---

## 🏗️ Project Setup
1. Open terminal (or VS Code terminal)
Then run:
# Go to the folder where you want to clone the project
cd ~/Downloads   # or wherever you prefer

2. Clone the repository
git clone https://github.com/SrinivasPujar18/QuizApp_usingDjango-and-Vue.js.git

3. Enter the project directory
cd QuizApp_usingDjango-and-Vue.js

⚙️ Setup for Backend (Django)
# Create virtual environment
python -m venv env

# Activate environment
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver

💻 Setup for Frontend (Vue.js)
If the Vue.js app is inside a frontend folder:
cd frontend

# Install npm dependencies
npm install

# Start the Vue.js development server
npm run serve


✅ Summary
Task	Command
Clone repo	git clone https://github.com/SrinivasPujar18/QuizApp_usingDjango-and-Vue.js.git
Enter folder	cd QuizApp_usingDjango-and-Vue.js
Setup backend	pip install -r requirements.txt → python manage.py runserver
Setup frontend	npm install → npm run serve


---
🔗 API Endpoints (Examples)
Endpoint	Method	Description
/api/quizzes/	GET	Get list of all quizzes
/api/quizzes/<id>/	GET	Get quiz details
/api/quizzes/submit/	POST	Submit quiz answers
/api/users/register/	POST	Register new user
/api/users/login/	POST	Login user
---



🤝 Contributing
Contributions are welcome!
1. Fork the repository
2. Create your feature branch (git checkout -b feature-name)
3. Commit your changes (git commit -m "Add feature")
4. Push to your branch (git push origin feature-name)
5. Open a Pull Request
---

-> Run with the help of 'url' in local server by:
http://127.0.0.1:8000/ ---> for "home.html" frontend file
http://127.0.0.1:8000/admin/ ---> for admin file
http://127.0.0.1:8000/api/get-quiz/ ---> for QuizCategory Questions and Answers
http://127.0.0.1:8000/quiz/?Category=Fullstack ---> for "Fullstack" category questions

👨‍💻 Author

Srinivasa G Pujar
📧 srinivaspujar2001@gmail.com
🌐 https://github.com/SrinivasPujar18
---
