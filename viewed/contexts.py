from django.shortcuts import get_object_or_404
from products.models import Product


def viewed_contents(request):
    """
    Ensures that the cart contents are available when rendering every page. 
    """

    viewed = request.session.get('viewed', {})
    
    viewed_items = []
    total = 0
    product_count = 0
    for id, quantity in viewed.items():
        product = get_object_or_404(Product, pk=id)
        total += 1 * product.search_price
        product_count += 1
        viewed_items.append({'id': id, 'quantity': quantity, 'product': product})

    return { 'viewed_items': viewed_items, 'total': total, 'product_count': product_count }