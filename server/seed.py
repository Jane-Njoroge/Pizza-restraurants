from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

   
    print("Deleting data...")
RestaurantPizza.query.delete()
Pizza.query.delete()
Restaurant.query.delete()

print("Creating restaurants...")
shack = Restaurant(name="Karen's Pizza Shack", address="123 Pizza Lane")
bistro = Restaurant(name="Sanjay's Pizza", address="456 Bistro Blvd")
palace = Restaurant(name="Kiki's Pizza Palace", address="789 Palace Road")
restaurants = [shack, bistro, palace]

print("Creating pizzas...")
cheese = Pizza(name="Cheese Pizza", ingredients="Dough, Tomato Sauce, Cheese")
pepperoni = Pizza(name="Pepperoni Pizza", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
california = Pizza(name="California Pizza", ingredients="Dough, Sauce, Ricotta, Red Peppers, Mustard")
pizzas = [cheese, pepperoni, california]

print("Creating restaurant pizzas...")
pr1 = RestaurantPizza(restaurant=shack, pizza=cheese, price=10)
pr2 = RestaurantPizza(restaurant=bistro, pizza=pepperoni, price=12)
pr3 = RestaurantPizza(restaurant=palace, pizza=california, price=15)
restaurant_pizzas = [pr1, pr2, pr3]


db.session.add_all(restaurants)
db.session.add_all(pizzas)
db.session.add_all(restaurant_pizzas)
db.session.commit()

print("Seeding done!") 