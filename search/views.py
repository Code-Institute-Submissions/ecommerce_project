from django.shortcuts import render
from products.models import Product

def do_search(request):
    products = Product.objects.filter(product_name__icontains=request.GET['q'])
    return render(request, "viewproducts.html", {"products": products})