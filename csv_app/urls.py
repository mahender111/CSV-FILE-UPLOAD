from django.urls import path
from .import views


urlpatterns = [
    # path('',views.index,name='index_urls'),
    path('',views.product_Upload,name='product_Upload_urls'),

]
