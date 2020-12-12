from . import app
from .. import car
from flask import render_template, redirect, abort


@app.route("/")
def index():
    message = ""
    return render_template("control.html", message=message)


@app.route("/forwards", methods=["POST"])
def forwards():
    car.forward()
    message = "Moved Forwards!"
    return render_template("control.html", message=message)


@app.route("/backwards", methods=["POST"])
def backwards():
    car.backward()
    message = "Moved Backwards!"
    return render_template("control.html", message=message)


@app.route("/left", methods=["POST"])
def left():
    car.left()
    message = "Turned Left!"
    return render_template("control.html", message=message)


@app.route("/right", methods=["POST"])
def right():
    car.right()
    message = "Turned Right!"
    return render_template("control.html", message=message)