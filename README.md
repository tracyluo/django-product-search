# Django Product Search

A Django web application for searching products by description, category, and tags. Includes sample data and a modern, professional UI.

## Features
- Product search by description, category, and tags (combine search and filter options.)

📌 Example Scenario
Input Filters:

Category: "PC Laptops"

Tag: "Back to school sale"

Description contains: "HP"

Search Result:

Only products that are:

In the category "PC Laptops"

Tagged with "Back to school sale"

With a description containing the keyword "HP"

- Category hierarchy (parent/child)
Categories are organized hierarchically, allowing more flexible and precise searches.

Example Hierarchy:
Laptops (Parent)
├── PC Laptops (Child)
└── MacBooks (Child)

Search Behavior:
Selecting a Parent Category (e.g., Laptops):

Returns all products in the parent category and its child categories.

✅ Products: PC Laptops + MacBooks

Selecting a Child Category (e.g., PC Laptops):

Returns only products directly under that child category.

✅ Products: Only PC Laptops

Selecting a Child Category (e.g., MacBooks):

✅ Products: Only MacBooks

- Tag filtering

- Sample data population via management command

- Responsive, styled product list page

## Setup

### Prerequisites
- Python 3.8+
- Poetry (for dependency management)
- Django 4.x

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/tracyluo/django-product-search.git
   cd django-product-search
   ```
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Apply migrations:
   ```bash
   poetry run python manage.py migrate
   ```
4. Populate sample data:
   ```bash
   poetry run python manage.py populate_data
   ```
5. Run the development server:
   ```bash
   poetry run python manage.py runserver
   ```
6. Visit `http://127.0.0.1:8000/` in your browser.

7. Run unit test
     python manage.py test product

## Project Structure
```
product_search/
    product/
        management/
            commands/
                populate_data.py   # Management command to populate sample data
            data/
                product.py         # Sample product data
        models/
            category.py           # Category model
            product.py            # Product model
            tag.py                # Tag model
        templates/
            product/
                product_list.html # Product list template
        static/
            product/
                product_list.css  # CSS for product list page
    product_search/
        settings.py               # Django settings
        urls.py                   # URL configuration
```

## Usage
- Search for products by description, category, and tags using the main page.
- Use the management command to reset and repopulate sample data as needed.

## License
MIT

## Author
Tracy Luo
