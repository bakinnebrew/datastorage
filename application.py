from flask import Flask, render_template, request, redirect, session, url_for
from cs50 import SQL
import csv
from flask_session import Session
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQL("sqlite:///monsters.db")

@app.route ("/")
def index():
    rows = db.execute("SELECT * FROM monsters")
    return render_template("index.html", rows=rows)

@app.route ("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
             if request.files:

                file = request.files["filename"]

    return render_template('upload.html')