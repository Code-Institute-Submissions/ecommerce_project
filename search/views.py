from django.shortcuts import render
from products.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def do_search(request):
    products = Product.objects.filter(product_name__icontains=request.GET['q'])
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 64)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "viewproducts.html", {"products": products})