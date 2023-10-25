from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# ... your Flask app creation code ...



app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)

# Sample data
sample_data = [
    {"name": "Headphones", "description": "Sony Headphones", "price": 10.99, "category": "Electronics"},
    #{"name": "Product 2", "description": "Description for Product 2", "price": 19.99, "category": "Clothing"},
    #{"name": "Product 3", "description": "Description for Product 3", "price": 5.99, "category": "Books"},
    #{"name": "Product 4", "description": "Description for Product 4", "price": 49.99, "category": "Home & Garden"},
    #{"name": "Product 5", "description": "Description for Product 5", "price": 29.99, "category": "Electronics"},
    #{"name": "Product 6", "description": "Description for Product 6", "price": 15.99, "category": "Clothing"},
    #{"name": "Product 7", "description": "Description for Product 7", "price": 8.99, "category": "Books"},
    #{"name": "Product 8", "description": "Description for Product 8", "price": 59.99, "category": "Home & Garden"},
    #{"name": "Product 9", "description": "Description for Product 9", "price": 14.99, "category": "Electronics"},
    #{"name": "Product 10", "description": "Description for Product 10", "price": 12.99, "category": "Clothing"},
]

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:id>')
def product(id):
    product = Product.query.get(id)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        for data in sample_data:
            product = Product(name=data['name'], description=data['description'], price=data['price'], category=data['category'])
            db.session.add(product)
        db.session.commit()
    app.run(debug=True)
