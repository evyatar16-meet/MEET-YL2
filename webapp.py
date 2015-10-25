from flask import Flask, render_template, request;
app = Flask(__name__) 

@app.route('/meet/<x>/<y>')
def index(x,y):
	print(x+y)
	zz=int(x)+int(y)
	return render_template('index.html',z=zz)

@app.route('')
