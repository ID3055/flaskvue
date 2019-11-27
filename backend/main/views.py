from flask import Flask, render_template, jsonify
# from flask_cors import CORS
import random
from . import main

# app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")
# cors = CORS(main, resources={r"/api/*": {"origins": "*"}})


@main.route('/api/random')
def random_number():
    response = {'randomNumber': random.randint(1, 100)}
    return jsonify(response)


@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def index(path):
    return render_template("index.html")
