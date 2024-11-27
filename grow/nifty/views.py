from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def itc(request):
    return HttpResponse('The buyers are involved in stocks and the stock price is high')