from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
#def index():
#	return "<h1>Hello, World!</h1>"


#safe
#capitalize
#lower
#upper
#title
#trim
#striptags


def index():
	first_name = "Ray"
	stuff = "This is <strong>Bold</strong> Text"
	return render_template('index.html', first_name=first_name,
		stuff=stuff)


# localhost:5000/user/Ray
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', user_name=name)


# Create custom error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500