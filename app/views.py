# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    return render_template("index.html")

@app.route('/index.html')
def indexhtml():
    return render_template("index.html")

@app.route('/home.html')
def home():
    return render_template("home.html")

@app.route('/<path:path>')
def send(path):
  return app.send_static_file(path) 

@app.route('/multi.html')
def multi():
    return render_template("multi.html")

@app.route('/mobile.html')
def mobile():
    return render_template("mobile.html")

@app.route('/gallery.html')
def gallery():
    return render_template("gallery.html")

@app.route('/admin.html')
def admin():
    return render_template("admin.html")