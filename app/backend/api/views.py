from flask import jsonify

import random
from . import api


@api.route('/random')
def random_number():
    response = {'randomNumber': random.randint(1, 100)}
    return jsonify(response)
