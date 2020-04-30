from flask import Flask, render_template, url_for, request, redirect, flash
from logging import DEBUG

from user import User

app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.secret_key = '\xd3\xea\xeba\xe3c-2&1\xbd\x86\xf9X\xde\x02\xe1\xbd\x83\x9d\x81\xf5#\x11'

@app.route('/')
@app.route('/index')
def index():
  return render_template(
    'index.html',
    title='Description',
    text='You can freely use this web app. Just remember to give a few kudos!',
    user=User('David', 'Hasslehof')
  )

@app.route('/add', methods=['GET', 'POST'])
def add_bookmark():
  if request.method == 'POST':
    app.logger.debug('Request to add {0}'.format(request.form['book_url']))
    flash('Stored bookmark: [{}]'.format(request.form['book_url']))
    return redirect(url_for('index'))
  if request.method == 'GET':
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
  return render_template('500.html'), 500