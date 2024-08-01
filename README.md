# Business Management System

This is a Django-based business management system that helps manage customers, products, and orders.

## Features

- Customer management: Add, view, and manage customer details.
- Product management: Add, view, and manage product details.
- Order management: Create, view, and manage orders.

## Requirements

- Python 3.8+
- Django 3.2+

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/allyelvis/BusinessManagementSystem.git
    cd BusinessManagementSystem
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/` to access the application.

## Usage

- To access the admin interface, go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.
- The main interface allows you to view and manage customers, products, and orders.

## Project Structure

- `BusinessManagementSystem/`: The main project directory.
- `management/`: The app directory containing models, views, forms, and templates.
- `templates/management/`: HTML templates for the application.
- `static/`: Static files (CSS, JavaScript, images).

## Models

- **Customer**: Contains fields for name, email, phone, and address.
- **Product**: Contains fields for name, description, price, and stock.
- **Order**: Contains fields for customer, product, quantity, and order date.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or feedback, please contact [yourname@example.com].