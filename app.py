import os
import psycopg2
from flask import Flask
app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)

@app.route("/")
def index():
    return "Hello World from YOUR NAME in 3308"

@app.route("/db_test")
def db_test():
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()


# conn = None
# cur = None
# try:
#     conn = psycopg2.connect(DATABASE_URL)
#     cur = conn.cursor()

#     # SQL work goes here

#     conn.commit()
#     return "Success message here"
# except Exception as e:
#     if conn is not None:
#         conn.rollback()
#     return f"Database error: {e}"
# finally:
#     if cur is not None:
#         cur.close()
#     if conn is not None:
#         conn.close()
