from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from dotenv import load_dotenv
import os
from server.controllers.pizza_controller import pizza
from server.controllers.index_controller import index
from server.controllers.restaurant_controller import restaurant 
from server.controllers.restaurant_pizza_controller import restaurant_pizza
from server.db import db

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
})

migrate = Migrate()


app = Flask(__name__)

load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(pizza)
app.register_blueprint(index)
app.register_blueprint(restaurant)
app.register_blueprint(restaurant_pizza)

db.init_app(app)
migrate.init_app(app, db)

if __name__ == "__main__":
    app.run(debug=True, port=5555)
