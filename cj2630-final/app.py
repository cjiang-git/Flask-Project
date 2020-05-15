# *******************************************************
# Effects Tester Module
# Final
# ENGI E1006
# Charlie Jiang
# cj2630
# This is code for the final assignment
# *******************************************************



#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

#accesses HTML code in homepage.html
@app.route("/1006")
def test(): 
    return render_template("homepage.html")

#accesses HTML code in Fav_assign.html
@app.route("/FavoriteAssignment")
def favAss():
    return render_template("Fav_assign.html")

#accesses HTML code in FallC.html
@app.route("/My_Spring_Classes")
def fallC():
    return render_template("SpringC.html")




#start the server
if __name__ == "__main__":
    app.run()