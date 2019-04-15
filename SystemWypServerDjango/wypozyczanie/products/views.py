from django.shortcuts import render
from .models import Products
from django.http import HttpResponse

# Create your views here.

def article_list(request):
	products = Products.objects.all()
	return render(request, 'products/products_list.html',{'products':products})