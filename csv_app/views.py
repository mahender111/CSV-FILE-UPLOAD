from django.shortcuts import render
from django.http import HttpResponse
import csv
from datetime import datetime

from .models import (Product,)

# Create your views here.
# def index(request):
#     return HttpResponse('welcome to first page')


def product_Upload(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        print(decoded_file)
        reader = csv.DictReader(decoded_file)

        for row in reader:         
                my_model = Product()
                my_model.item_name = row['item_name']
                my_model.rate = row['rate']
                my_model.item_len = row['item_len']
                my_model.item_width = row['item_width']
                date_format = "%d/%m/%Y"  
               
                # my_model.valid_from = '2023-11-20'
                # my_model.valid_upto = '2099-12-1'
                
                my_model.valid_from = datetime.strptime(row['valid_from'], date_format).date()
                my_model.valid_upto = datetime.strptime(row['valid_upto'], date_format).date()
                my_model.valid_yn = row['valid_yn'].lower().capitalize()
                my_model.save()

    
    return render(request, 'product_Upload.html')
