from flask import Flask, request, jsonify
import psycopg2
import os
import time

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "devdb"),
        user=os.getenv("DB_USER", "devuser"),
        password=os.getenv("DB_PASSWORD", "devpass")
    )

def init_db():
    max_retries = 10
    for attempt in range(max_retries):
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL
                );
            """)
            conn.commit()
            cur.close()
            conn.close()
            print("Database initialized successfully.")
            return
        except Exception as e:
            print(f"Database init failed (attempt {attempt + 1}/{max_retries}): {e}")
            time.sleep(2)

    raise Exception("Could not initialize database after multiple retries.")

@app.route("/")
def hello():
    return "API läuft"

@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users ORDER BY id;")
    users = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(users)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s);", (name,))
    conn.commit()
    cur.close()
    conn.close()

    return {"message": "User created"}, 201

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
