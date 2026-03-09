from flask import Blueprint, render_template

add = Blueprint("add", __name__)


@add.route('/add')
def add_vehicle():
    return render_template("add.html")


