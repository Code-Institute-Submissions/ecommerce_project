from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def viewproducts(request):
    products = Product.objects.get_queryset().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 8)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'viewproducts.html', {'products': products}) 
    
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'viewproducts.html', {'products': products})
    
def get_index(request):
    return render(request, 'index.html')
    
    
 
    

    
    
    
