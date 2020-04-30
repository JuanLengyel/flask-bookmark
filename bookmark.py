from flask import Flask, render_template, url_for

from user import User

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template(
    'index.html',
    title='Description',
    text='You can freely use this web app. Just remember to give a few kudos!',
    user=User('David', 'Hasslehof')
  )

@app.route('/add')
def add_bookmark():
  return render_template('add.html')