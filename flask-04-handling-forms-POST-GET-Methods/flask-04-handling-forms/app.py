# Import Flask modules
from flask import Flask, render_template, request

# Create an object named app
app = Flask(__name__)

# Create welcome page with main.html file and assign it to the root path
@app.route("/")
def welcome():
    return render_template("main.html", name="Azalaya")

# Write a function named `greet` which uses template file named `greet.html` given under 
# `templates` folder. it takes parameters from query string on URL, assign that parameter 
# to the 'user' variable and sent that user name into the html file. If it doesn't have any parameter, warning massage is raised
@app.route("/greet")
def greet():
    if "user" in request.args:
        user = request.args["user"]
        return render_template("greet.html", user=user)
    else:
        return "Sorry, you need to have a parameter 'user' in the url"


# Write a function named `login` which uses `GET` and `POST` methods, 
# and template files named `login.html` and `secure.html` given under `templates` folder 
# and assign to the static route of ('login')
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if password == 'clarusway':
            return render_template("secure.html", user=username)
        else:
            return render_template("login.html", control=True, user=username)
    else:
        return render_template("login.html", control=False)

# Add a statement to run the Flask application
if __name__ == "main":
    app.run(debug=True)