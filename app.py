from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import "auth/auth"
import hashlib

app = Flask(__name__)

app.secret_key = "mwebfailusgdfaiweflauksbdflakjbsdfiquwe"

@app.route("/")

def route1():
    if "user" in session:
        return render_template("welcome.html", name= session["user"])
    return render_template("index.html")

@app.route("/logout")

def logout():
    session.pop("user")
    return redirect("/")

@app.route("/login", methods=['GET', 'POST'])

def login():
    return render_template("login.html")

@app.route("/loginauth", methods=['GET', 'POST'])

def route2():
    #print request.method

    line = i.split(",")
    user = request.form["user"]
    passwd = request.form["pass"]
    
    if authenticate(user, passwd):
            return "login successful <a href='/'>back home</a>"
    return "login unsuccessful. <a href='/login'>try again</a>"

@app.route("/register", methods=['GET', 'POST'])

def route3():
    return render_template("register.html")

@app.route("/registerauth", methods=['GET', 'POST'])

def route4():
    occu = open("data/auth.csv", "a")
    hashobject = hashlib.sha256(request.form["pass"])
    hexdig = hashobject.hexdigest()
    occu.write(request.form["user"] + "," + hexdig + "\n")

    return "register successful <a href='/'>back home</a>"

if __name__ == "__main__":
    app.debug = True
    app.run()
