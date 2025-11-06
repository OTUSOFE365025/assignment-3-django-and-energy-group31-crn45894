############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import Product


def populate_database():
    Product.objects.all().delete()  # clear old data

    Product.objects.create(upc="123456789012", name="Apple", price=0.99)
    Product.objects.create(upc="987654321098", name="Banana", price=0.59)
    Product.objects.create(upc="111222333444", name="Milk", price=3.49)
    Product.objects.create(upc="555666777888", name="Bread", price=2.29)

    print(" Database populated with sample products.")
    print("Current products in database:\n")
    for p in Product.objects.all():
        print(f"UPC: {p.upc} | Name: {p.name} | Price: ${p.price}")



def scan_product():
    print("\n--- Scan a Product ---")
    upc_input = input("Enter product UPC code: ")

    try:
        product = Product.objects.get(upc=upc_input)
        print(f"\n Product Found")
        print(f"Name: {product.name}")
        print(f"Price: ${product.price}")
    except Product.DoesNotExist:
        print("\n Product not found. Please try again.")


if __name__ == "__main__":
    populate_database()
    scan_product()
