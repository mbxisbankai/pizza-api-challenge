from flask import Blueprint, make_response

index = Blueprint('index', __name__)

@index.route('/')
def get_index():
    return make_response({"message": "Welcome to the Pizza API!"}, 200)
