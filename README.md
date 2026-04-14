# 🎓 Student Management System

A full-stack web application to manage student records using Flask and MySQL, deployed using modern DevOps tools.

---

## 🚀 Features

* Add student details
* Update student records
* Delete students
* View all students

---

## 🛠 Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS
* **Database:** MySQL

---

## ⚙️ DevOps & Deployment

* **Docker:** Containerized Flask application
* **Jenkins:** Automated CI/CD pipeline
* **AWS EC2:** Cloud deployment

---

## 🐳 Running with Docker

```bash
docker build -t student-app .
docker run -d -p 5000:5000 student-app
```

---

## ⚙️ Jenkins Pipeline

* Pulls code from GitHub
* Builds Docker image
* Runs container automatically

---

## ☁️ AWS Deployment

* EC2 instance created using Boto3
* Application deployed inside Docker container on EC2

---

## ▶️ Local Setup (Without Docker)

```bash
git clone https://github.com/your-username/student-management-system.git
cd student-management-system

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python app/app.py
```

---

## 📌 Author

Aman Kumar Rai
