from server.db import db
from sqlalchemy_serializer import SerializerMixin

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