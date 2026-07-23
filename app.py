import os
import psycopg2
from flask import Flask
app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)

@app.route("/")
def index():
    return "Hello World from YOUR NAME in 3308"
