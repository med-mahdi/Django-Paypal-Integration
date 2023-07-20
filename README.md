# Django PayPal Integration

This is a Django web application that demonstrates how to integrate PayPal payments using the PayPal REST API and PayPal IPN (Instant Payment Notification) feature. The application allows users to make payments for a product using PayPal's sandbox environment for testing purposes.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- Django
- PayPal account (to use the sandbox environment)

## Getting Started

1. Clone the repository using the following command:

```bash
git clone https://github.com/med-mahdi/Django-Paypal-Integration.git

### Create and activate a virtual environment (optional but recommended):
python -m venv venv

> On macOS and Linux:
source venv/bin/activate

> On Windows:
venv\Scripts\activate

### Install the required packages:
pip install -r requirements.txt

### Apply the database migrations:
python manage.py migrate

### Create a superuser (for accessing the Django admin interface):
python manage.py createsuperuser

### Run the development server:
python manage.py runserver
Access the application in your web browser at http://127.0.0.1:8000/.
