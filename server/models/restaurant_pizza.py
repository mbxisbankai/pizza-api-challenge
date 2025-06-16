from server.db import db
from sqlalchemy import CheckConstraint
from sqlalchemy_serializer import SerializerMixin

class RestaurantPizza( db.Model, SerializerMixin ):
    __tablename__ = 'restaurant_pizzas'

    __table_args__ = (
        CheckConstraint('price >= 1 AND price <= 30', name='check_price_range'),
    )

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')

    serialize_rules = ('-restaurant', 'pizza')

    def __repr__(self):
        return f"<RestaurantPizza {self.id}: Price: {self.price}, pizza_id: {self.pizza_id}, restaurant_id: {self.restaurant_id}>"
