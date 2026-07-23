import os
import psycopg2
from flask import Flask
app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")

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


@app.route("/db_create")
def db_create():
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
        """)
        conn.commit()
    except Exception as e:
        if conn is not None:
            conn.rollback()
        return f"Database error: {e}"
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    return "Basketball Table Created"

@app.route('/db_insert')
def inserting():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Basketball (First, Last, City, Name, Number)
            VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
            ('Theodore', 'Matthews', 'CU Boulder', 'Tech Titans', 3308);
        """)
        conn.commit()
    except Exception as e:
        if conn is not None:
            conn.rollback()
        return f"Database error: {e}"
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    return "Basketball Table Populated"


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
