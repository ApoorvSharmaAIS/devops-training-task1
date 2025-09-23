from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DB_NAME = "student.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            marks INTEGER NOT NULL
        )
    ''')
    
    # add sample data
    c.execute("INSERT INTO students (name, marks) VALUES ('Apoorv', 85)")
    c.execute("INSERT INTO students (name, marks) VALUES ('Ram', 99)")
    c.execute("INSERT INTO students (name, marks) VALUES ('Krishn', 100)")

    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT name, AVG(marks) FROM students GROUP BY name")
    results = c.fetchall()
    conn.close()
    return render_template("index.html", results=results)

# Uncomment once to initialize the DB
# init_db()

app.run(host='0.0.0.0', port=8000)
