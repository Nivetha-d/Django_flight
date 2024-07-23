from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests

def search_flights(request):
    return render(request, 'flights/search.html')