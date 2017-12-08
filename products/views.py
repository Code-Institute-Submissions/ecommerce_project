from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
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
    
def show_category(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    parent = None
    root = Category.objects.all()

    for slug in category_slug[:-1]:
        parent = root.get(parent=parent, slug = slug)

    try:
        instance = Category.objects.get(parent=parent,slug=category_slug[-1])
    except:
        instance = get_object_or_404(Product, slug = category_slug[-1])
        return render(request, "viewproducts.html", {'instance':instance})
    else:
        return render(request, 'categories.html', {'instance':instance})
    
    

    
    
    
