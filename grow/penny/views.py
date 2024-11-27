from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bengalsteels(request):
    return HttpResponse('this stock is a penny stock price is low')