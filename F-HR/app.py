from flask import Flask,render_template,request
import sqlite3
#import webview
import os
import traceback
import sys

###################################################################################################################################################
# System Database Section #
###################################################################################################################################################

db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
cr = db.cursor()
cr.execute(f"CREATE TABLE IF NOT EXISTS Emploees(Name TEXT , Id INTEGER , Address TEXT, Mobile INTEGER , Email TEXT , Gender TEXT , MStatuts TEXT , Salary INTEGER , BirthDay DATE , VactionNum INTEGER , AVactionNum INTEGER)")

###################################################################################################################################################
# Applaction Section #
###################################################################################################################################################

app = Flask(__name__)

###################################################################################################################################################
# Pages Setion #
###################################################################################################################################################
@app.route('/') 
def Home():
    return render_template('Home.html', title = "Home Page")

@app.route('/LogIn') 
def LogIn():
    return render_template('Log in.html', title = "Log In Page")

@app.route('/AddEmployee') 
def AddEmployee():
    return render_template('Add Employee.html', title = "Add Employee Page")

@app.route('/HRProfile') 
def HRProfile():
    return render_template('HR .html', title = "Add Employee Page")
###################################################################################################################################################
# Running Setion #
###################################################################################################################################################

if __name__  == "__main__":
    app.run()