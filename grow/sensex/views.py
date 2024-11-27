from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def railware(request):
    return HttpResponse('the stock is downfall now ')

