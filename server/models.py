from server.db import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import CheckConstraint

class Pizza( db.Model, SerializerMixin ):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')

    serialize_rules = ('-restaurant_pizzas',)

    def __repr__(self):
        return f'<Pizza {self.id}: {self.name}, Ingredients: [{self.ingredients}]>'
    
class Restaurant( db.Model, SerializerMixin ):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    restaurant_pizzas = db.relationship(
        'RestaurantPizza',
        back_populates='restaurant',
        cascade='all, delete-orphan'
    )

    serialize_rules = ('-restaurant_pizzas',)

    def __repr__(self):
        return f'<Restaurant {self.id}: {self.name}, {self.address}>'
    

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