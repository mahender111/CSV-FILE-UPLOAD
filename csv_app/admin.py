from django.contrib import admin
from .models import Product

# Register your models here.
class Product_Admin(admin.ModelAdmin):
    list_display = [
        'id',
        'item_name',
        'rate',
        'item_len',
        'item_width',
        'valid_from',
        'valid_upto',
        'valid_yn',
        
    ]
    


    list_filter =['item_name','rate','item_len']
    search_fields = ['item_name','rate','item_len']
    
# ----------------------------------------------------------------register-admin page-----------------------------------------------------
# register admin page

    
admin.site.register(Product,Product_Admin)
