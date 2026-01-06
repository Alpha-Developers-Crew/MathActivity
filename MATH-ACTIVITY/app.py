from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/maths")
def maths():
    return render_template("maths.html")

@app.route("/activity")
def activity():
    return render_template("activity.html")

@app.route("/consecutiveNumbers")
def consecutiveNumbers():
    return render_template("consecutiveNumbers.html")

@app.route("/cryptarithms")
def cryptarithms():
    return render_template("cryptarithms.html")

@app.route("/digitalRoots")
def digitalRoots():
    return render_template("digitalRoots.html")

@app.route("/divisibilityRules")
def divisibilityRules():
    return render_template("divisibilityRules.html")

@app.route("/evenOdd")
def evenOdd():
    return render_template("evenOdd.html")

@app.route("/fibonnaciSeries")
def fibonnaciSeries():
    return render_template("fibonnaciSeries.html")

app.run(debug=True)