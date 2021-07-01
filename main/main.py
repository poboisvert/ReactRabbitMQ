from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
# SQL config
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'

CORS(app)

db = SQLAlchemy(app)

# Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    description = db.Column(db.String(200))
    image = db.Column(db.String(200))

class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique') # Must be Unique


# Route
@app.route('/')
def index():
    return 'Server ON'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')