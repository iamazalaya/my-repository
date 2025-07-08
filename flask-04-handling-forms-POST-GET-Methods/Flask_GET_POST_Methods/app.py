# Import Flask modules
from flask import Flask, render_template, request

import math
# Create an object named app
app = Flask(__name__)


# create a function named "lcm" which calculates a least common multiple values of two numbers. 
def lcm(a, b):
    return math.lcm(a, b)


# Create a function named `index` which uses template file named `index.html` 
# send two numbers as template variable to the app.py and assign route of no path ('/') 
@app.route("/")
def index():
    return render_template("index.html", methods=["GET"])




# calculate sum of them using "lcm" function, then sent the result to the 
# "result.hmtl" file and assign route of path ('/calc'). 
# When the user comes directly "/calc" path, "Since this is a GET request, LCM has not been calculated" string returns to them with "result.html" file
@app.route("/calc", methods=["GET", "POST"])
def calc():
    if request.method== "POST":
        a = int(request.form.get("number1"))
        b = int(request.form.get("number2"))
        
        result = lcm(a, b)
        
        return render_template(
            "result.html", 
            developer_name="Azalaya", 
            lcm=result, 
            result1=a, 
            result2=b
        )
    else:
        return render_template("result.html", developer_name="Azalaya")


# Add a statement to run the Flask application which can be debugged.
if __name__ == "main":
    app.run(debug=True)