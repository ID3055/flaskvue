from flask import render_template, jsonify
from . import manage

@manage.route('/manage.html', defaults={'path': ''})
@manage.route('/<path:path>')
def index(path):
    return render_template("manage.html")
