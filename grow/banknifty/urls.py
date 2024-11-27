from banknifty.views import *
from django.urls import path
urlpatterns = [
    path('hdfc/',hdfc,name='hdfc'),
    path('icici/',icici,name='icici'),
]

