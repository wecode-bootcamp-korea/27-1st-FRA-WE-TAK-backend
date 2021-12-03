import os
import django
import csv
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FRA_WE_BACK.settings")
django.setup()
from products.models import MainCategory, SubCategory, Product, Image
"""
CSV_PATH = './main_categories.csv'

with open(CSV_PATH, newline='') as csvfile:
     data_reader = csv.DictReader(csvfile)
     for row in data_reader:
         print(row)
         MainCategory.objects.create(
             name = row['name']
         )


CSV_PATH = './sub_categories.csv'


with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        SubCategory.objects.create(
            kr_name = row['kr_name'],
            en_name = row['en_name'],
            thumbnail_url = row['thumbnail_url'],
            main_category_id = row['main_category_id']
        )

CSV_PATH = './products.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        if SubCategory.objects.filter(id=row['sub_category_id']).exists():
            Product.objects.create(
                kr_name            = row['kr_name'],
                en_name            = row['en_name'],
                price              = row['price'],
                title              = row['title'],
                rating             = row['rating'],
                description        = row['description'],
                sub_category_id    = row['sub_category_id']
            )

CSV_PATH = './images.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        Image.objects.create(
            url = row['url'],
            product_id = row['product_id'],
        )
"""