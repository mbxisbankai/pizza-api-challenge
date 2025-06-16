from server.db import db
from sqlalchemy_serializer import SerializerMixin

class Pizza( db.Model, SerializerMixin ):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')

    serialize_rules = ('-restaurant_pizzas',)

    def __repr__(self):
        return f'<Pizza {self.id}: {self.name}, Ingredients: [{self.ingredients}]>'