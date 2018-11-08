from flask import Flask, flash, redirect, render_template, request, session, abort 
import os 
from sqlalchemy.orm import sessionmaker
from tabledef import * 
from passlib.hash import sha256_crypt 
engine = create_engine('sqlite:///pomodoro_data.db', echo = True)

app = Flask(__name__)

@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		return render_template('index.html') ##We are in Baby!' # ტემპლეტს მივარენდერებთ აქაც


@app.route('/login', methods = ['POST'])
def login():

	POST_USERNAME = str(request.form['username'])
	POST_PASSWROD = str(request.form['password'])

	Session = sessionmaker(bind = engine)
	s = Session()

	#სქლ დატას წამოღება
	
	query = s.query(User).filter_by(username = POST_USERNAME)
	
	if query.first():
		authenticated = sha256_crypt.verify(POST_PASSWROD,query[0].password)
		if authenticated:
			session['logged_in'] = True
		else:
			flash('Wrog Password!')
	return home()

#გამოსვლა (შესაძლოა სხვა ხერხითაც)
@app.route('/logout')
def logout():
	session['logged_in'] = False
	return home()

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug = True, host = '0.0.0.0', port = 4000)	
