from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


class Restaurant(db.Model, SerializerMixin):
    __tablename__ = "restaurants"

id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String, nullable=False)
address = db.Column(db.String)

restaurant_pizzas = db.relationship("RestaurantPizza", back_populates="restaurant")
serialize_rules = ("-restaurant_pizzas.restaurant", "restaurant_pizzas.pizza")

def __repr__(self):
    return f"<Restaurant {self.name}>"
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String, nullable=False)
ingredients = db.Column(db.String)

restaurant_pizzas = db.relationship("RestaurantPizza", back_populates="pizza")
serialize_rules = ("-restaurant_pizzas.pizza",)

def __repr__(self):
    return f"<Pizza {self.name}, {self.ingredients}>"
