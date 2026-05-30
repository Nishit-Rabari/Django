from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def infoNishit(requests):
    return HttpResponse("<h3>Nishit</h3><h4>Roll:158</h4><h4>Div:D5</h4>")

def Detail(requests):
    return HttpResponse("<h3>Welcome to Nishit</h3>")