from flask import Blueprint, make_response, request
from server.models.pizza import Pizza
from server.db import db

pizza = Blueprint('pizza', __name__)

@pizza.route('/pizzas', methods = ['GET', 'POST'])
def get_pizzas():

    if request.method == 'GET':
        pizzas = [p.to_dict() for p in Pizza.query.all()]

        response = make_response(
            pizzas,
            200
        )
        return response
    elif request.method == 'POST':
        new_pizza = Pizza(
            name = request.form.get('name'),
            ingredients = request.form.get('ingredients')
        )
        db.session.add(new_pizza)
        db.session.commit()

        response = make_response( new_pizza.to_dict(), 201 )
        return response

@pizza.route('/pizzas/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
def pizza_by_id(id):
    pizza = Pizza.query.filter(Pizza.id == id).first()
    
    if request.method == 'GET':
        response = make_response(
            pizza.to_dict(),
            200
        )
        return response
    
    elif request.method == 'PATCH':
        for attr in request.form:
            setattr(pizza, attr, request.form.get(attr))
        db.session.add(pizza)
        db.session.commit()

        response = make_response(
            pizza.to_dict(),
            200
        )
        return response
    
    elif request.method == 'DELETE':
        db.session.delete(pizza)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Pizza deleted."
        }
        return make_response(response_body, 200)