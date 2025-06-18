from flask import Blueprint, make_response, request
from ..models import Restaurant
from server.db import db

restaurant = Blueprint('restaurant', __name__)

@restaurant.route('/restaurants', methods = ['GET', 'POST'])
def get_restaurants():

    if request.method == 'GET':
        restaurants = [r.to_dict() for r in Restaurant.query.all()]

        response = make_response(
            restaurants,
            200
        )
        return response
    
    elif request.method == 'POST':
        new_restaurant = Restaurant(
            name = request.form.get('name'),
            address = request.form.get('address')
        )
        db.session.add(new_restaurant)
        db.session.commit()

        response = make_response( new_restaurant.to_dict(), 201 )
        return response

@restaurant.route('/restaurants/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
def restaurant_by_id(id):
    restaurant = Restaurant.query.filter(Restaurant.id == id).first()

    if not restaurant:
        return make_response({"error": "Restaurant not found"}, 404)
    
    if request.method == 'GET':
        response = make_response(
            restaurant.to_dict(),
            200
        )
        return response
    
    elif request.method == 'PATCH':
        for attr in request.form:
            setattr(restaurant, attr, request.form.get(attr))
        db.session.add(restaurant)
        db.session.commit()

        response = make_response(
            restaurant.to_dict(),
            200
        )
        return response
    
    elif request.method == 'DELETE':
        db.session.delete(restaurant)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "No Content."
        }
        return make_response(response_body, 204)