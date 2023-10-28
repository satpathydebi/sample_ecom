from flask import Flask, render_template, request,session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# ... your Flask app creation code ...



app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
image_url = db.Column(db.String(200))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)

# Sample data
sample_data = [
    {
        "name": "Headphones",
        "description": "Sony Headphones",
        "price": 10.99,
        "category": "Electronics",
        "image_url": "https://media.istockphoto.com/id/1389603578/photo/laptop-blank-screen-on-wood-table-with-blurred-coffee-shop-cafe-interior-background-and.jpg?s=1024x1024&w=is&k=20&c=p7ApF_YFB25U09t6h37Fg8RnWPkQ_eT0zMUASAR0wcU="  # Add an image URL
    },
    {
        "name": "Laptop",
        "description": "Dell",
        "price": 199.99,
        "category": "Computer",
        "image_url": "https://media.istockphoto.com/id/1389603578/photo/laptop-blank-screen-on-wood-table-with-blurred-coffee-shop-cafe-interior-background-and.jpg?s=1024x1024&w=is&k=20&c=p7ApF_YFB25U09t6h37Fg8RnWPkQ_eT0zMUASAR0wcU="  # Add an image URL
    }
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
# ... (previous code) ...

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        products = Product.query.filter(Product.name.ilike(f'%{search_query}%')).all()
    else:
        products = []

    return render_template('search.html', products=products)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # You can implement your cart functionality here.
    # For now, let's just store the product ID in a session variable.
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    return redirect('/')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        for data in sample_data:
            product = Product(name=data['name'], description=data['description'], price=data['price'], category=data['category'])
            db.session.add(product)
        db.session.commit()
    app.run(debug=True)
