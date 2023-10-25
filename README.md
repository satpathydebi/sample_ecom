# Sample E-commerce Portal

This is a sample e-commerce portal created using Flask and SQLite as a database. The project is a starting point for building a simple e-commerce website with basic product listing and viewing functionality.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Adding Products](#adding-products)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Displays a list of products on the homepage.
- Allows users to click on a product to view its details.
- Supports the addition of new products with different categories.
- Demonstrates the use of Flask, SQLAlchemy, and Flask-Migrate.

## Prerequisites

To run this project, you need the following installed on your system:

- Python (3.7 or higher)
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

You can install Flask and the necessary extensions using pip:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```
## Getting Started
Clone this repository to your local machine:
    git clone https://github.com/satpathydebi/sample_ecom.git
    cd sample_ecom
Create a virtual environment (optional but recommended):
    python -m venv venv
Activate the virtual environment:
 On Windows:
    venv\Scripts\activate
 On macOS and Linux:
    source venv/bin/activate
Run the Flask application:
python app.py
The application will be accessible at http://localhost:5000.

## Usage
Visit http://localhost:5000 in your web browser to access the e-commerce portal. You can click on the products to view their details.

## Adding Products
To add new products with different categories, you can modify the sample_data list in the app.py file:

sample_data = [
    {"name": "Product 1", "description": "Description for Product 1", "price": 10.99, "category": "Electronics"},
    {"name": "Product 2", "description": "Description for Product 2", "price": 19.99, "category": "Clothing"},
    # Add more products here
]
Each dictionary represents a product with its name, description, price, and category. You can add or modify products as needed.

## Project Structure
The project structure is organized as follows:

app.py: The main Flask application and database setup.
templates/: Contains HTML templates for rendering web pages.
ecommerce.db: The SQLite database file.
README.md: This documentation.
## Contributing
Contributions are welcome! If you have suggestions, improvements, or bug fixes, please create an issue or a pull request.

# Steps to update the database schema(Add Category):

## Install Flask-Migrate:
pip install Flask-Migrate
## Initialize the migration environment:
flask db init
This will create a migrations folder in your project directory.

## Create a migration:

flask db migrate -m "Add category column"

Ex. flask db migrate -m "Electronics"
This command generates a migration script based on the changes made to your models.

## Apply the migration to update the database schema:

flask db upgrade
After running these commands, your database schema will be updated to include the "category" column.