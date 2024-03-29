from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route Decorator
#@app.route('/')
#def index():
#    return '<h1>Hello World!</h1>'

@app.route('/')
def index():
    first_name = "Ray"
    stuff = "This is bold text"
    favorite_toppings = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template('index.html',
                           first_name=first_name,
                           stuff=stuff,
                           favorite_toppings=favorite_toppings)

# localhost:5000/user/name
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',
                           user_name=name,
                           stuff=stuff)


# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
