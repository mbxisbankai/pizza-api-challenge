from server.db import db
from server.models import Pizza, Restaurant, RestaurantPizza
from server.app import app


with app.app_context():
    print("🌱 Seeding data...")

    # Clear existing data
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    # Create some restaurants
    r1 = Restaurant(name="Mama Mia Pizzeria", address="123 Pizza Street")
    r2 = Restaurant(name="Slice of Heaven", address="456 Cheese Ave")

    db.session.add_all([r1, r2])
    db.session.commit()

    # Create some pizzas
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    p3 = Pizza(name="Hawaiian", ingredients="Tomato, Mozzarella, Pineapple, Ham")

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    # Create some restaurant_pizza associations
    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=11, restaurant_id=r2.id, pizza_id=p3.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("✅ Done seeding!")
