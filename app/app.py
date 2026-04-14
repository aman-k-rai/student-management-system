from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import time
import os

app = Flask(__name__)

#connect to mysql
import time
import mysql.connector

# connect to mysql with retry
for i in range(10):
    try:
        db = mysql.connector.connect(
            host="mysql",
            user="root",
            password=os.getenv("MYSQL_ROOT_PASSWORD"),
            database="studentdb"
        )
        print("DB connected")
        break

    except Exception as e:
        print("Waiting for MySQL...", e)
        time.sleep(3)
else:
    raise Exception("Could not connect to MySQL")


cursor = db.cursor()


# Home Route - Display all students

@app.route('/')
def index():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('index.html', students=students)


# Add Students

@app.route('/add', methods=['POST'])
def add_students():
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", (name, age, grade))
        db.commit()
        return redirect(url_for('index'))

# Delete Students

@app.route('/delete/<int:id>', methods=['POST'])
def delete_students(id):
        cursor.execute("DELETE FROM students WHERE id=%s", (id,))
        db.commit()
        return redirect(url_for("index"))


# Edit Students
@app.route('/edit/<int:id>')
def edit_student(id):
      cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
      student = cursor.fetchone()
      return render_template('edit.html', student=student)

# Update Students
@app.route('/update/<int:id>', methods=['POST'])
def update_students(id):
      name = request.form['name']
      age = request.form['age']
      grade = request.form['grade']
      cursor.execute("UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s", (name, age, grade, id))
      db.commit()
      return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)