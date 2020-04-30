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

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
  return render_template('500.html'), 500