from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/Home')

def home():

	return render_template('Home page.html')

@app.route('/About')

def about():

	return render_template('about.html')

@app.route('/Contact')

def contact():

	return render_template('contact.html')

@app.route('/result', methods=['POST'])
def result():
	email = request.form['email']
	message = request.form['message']
	return render_template('result.html',email=email,message=message)
	

if __name__ == '__main__':
	app.debug = True
	app.run()
