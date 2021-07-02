import requests
from dataclasses import dataclass

from flask import Flask, jsonify, abort

from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

from producer import publish


app = Flask(__name__)
# SQL config
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'

CORS(app)

db = SQLAlchemy(app)

# Model
@dataclass
class Product(db.Model):
    id: int
    title: str
    description: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    description = db.Column(db.String(200))
    image = db.Column(db.String(200))
    # Create the table product

@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique') # Must be Unique
    # Create the table product_user


# Route - All products
@app.route('/api/products')
def index():
    return jsonify(Product.query.all())

# Route / - Test if server is ON
@app.route('/')
def home():
    return 'Server ON'

# Route / - Test if server is ON
@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://host.docker.internal:8000/api/user') # Return a random user
    json = req.json()

    try:
        productUser = ProductUser(user_id=json['id'], product_id=id) # Match the id user and id product
        db.session.add(productUser)
        db.session.commit()

        publish('product_liked', id)
    except:
        abort(400, 'You already liked this product')

    return jsonify({
        'message': 'success'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')