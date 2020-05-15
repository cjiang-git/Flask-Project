# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/1006")
def test(): 
    return render_template("homepage.html")

@app.route("/FavoriteAssignment")
def favAss():
    return render_template("Fav_assign.html")

@app.route("/My_Fall_Classes")
def fallC():
    return render_template("FallC.html")




#start the server
if __name__ == "__main__":
    app.run()