from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hdfc(request):
    return HttpResponse('stock is very high cost')
def icici(request):
    return HttpResponse('this icici is low now')