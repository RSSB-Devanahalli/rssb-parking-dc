from flask import Blueprint, render_template

search = Blueprint("search", __name__)

@search.route('/search')
def search_vehicle():
    return render_template("search.html")


