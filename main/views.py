from django.shortcuts import render
from django.utils import timezone


# Create your views here.

def main_page(request):
    return render(request, 'main.html')
