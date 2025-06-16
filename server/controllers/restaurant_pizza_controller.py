from flask import Blueprint, make_response, request
from server.models.restaurant_pizza import RestaurantPizza
from server.db import db
from sqlalchemy.exc import IntegrityError

restaurant_pizza = Blueprint('restaurant_pizza', __name__)

@restaurant_pizza.route('/restaurant_pizzas', methods=['GET', 'POST'])
def get_restaurant_pizzas():

    if request.method == 'GET':
        restaurant_pizzas = [rp.to_dict() for rp in RestaurantPizza.query.all()]
        return make_response(restaurant_pizzas, 200)

    elif request.method == 'POST':
        price = request.form.get('price')
        restaurant_id = request.form.get('restaurant_id')
        pizza_id = request.form.get('pizza_id')

        # Check if all required fields are provided
        if not all([price, restaurant_id, pizza_id]):
            return make_response({"error": "Missing required fields"}, 400)

        try:
            price = int(price)
        except ValueError:
            return make_response({"error": ["Price must be an integer"]}, 400)

        if price < 1 or price > 30:
            return make_response({"error": ["Price must be between 1 and 30"]}, 400)

        new_restaurant_pizza = RestaurantPizza(
            price=price,
            restaurant_id=restaurant_id,
            pizza_id=pizza_id
        )

        try:
            db.session.add(new_restaurant_pizza)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return make_response({"error": "Invalid restaurant or pizza ID"}, 400)

        return make_response(new_restaurant_pizza.to_dict(), 201)
@restaurant_pizza.route('restaurant_pizzas/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
def get_rp_by_id(id):
    restaurant_pizza = RestaurantPizza.query.filter(RestaurantPizza.id == id).first()

    if not restaurant_pizza:
        return make_response({"error": "Restaurant Pizza not found"}, 400)
    
    if request.method == 'GET':
        response = make_response(
            restaurant_pizza.to_dict(),
            200
        )
        return response
    
    elif request.method == 'PATCH':
        for attr in request.form:
            setattr(restaurant_pizza, attr, request.form.get(attr))
        db.session.add(restaurant_pizza)
        db.session.commit()

        response = make_response(
            restaurant_pizza.to_dict(),
            200
        )
        return response
    
    elif request.method == 'DELETE':
        db.session.delete(restaurant_pizza)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "No content"
        }

        response = make_response(
            response_body,
            204
        )
        return response

