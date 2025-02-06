from flask import Flask, jsonify, request
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{"id": r.id, "name": r.name, "address": r.address} for r in restaurants])

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{"id": p.id, "name": p.name, "ingredients": p.ingredients} for p in pizzas])

@app.route('/restaurant_pizzas', methods=['POST'])
def add_restaurant_pizza():
    data = request.get_json()
    rp = RestaurantPizza(price=data['price'], restaurant_id=data['restaurant_id'], pizza_id=data['pizza_id'])
    db.session.add(rp)
    db.session.commit()
    return jsonify({"id": rp.id, "price": rp.price}), 201