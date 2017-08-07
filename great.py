from flask import Flask, render_template, request, redirect, session

import random
app = Flask(__name__)
app.secret_key = 'mySecret'

@app.route('/')

def index():
	if 'random' not in session:
		session['random'] = random.randrange(0,100)
		print session
	if 'store' not in session:
		session['store'] = 0
		print session 
	print session	
	return render_template('index.html')

@app.route('/process', methods=['POST'])

def guess():
	session['store'] = int(request.form['number'])

	print request.form
	print session
	return redirect('/')

# @app.route('/reset', methods=['POST'])
# def reset():
# 	return redirect('/')


app.run(debug=True)