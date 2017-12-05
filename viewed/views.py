from django.shortcuts import render, redirect, reverse, get_object_or_404

def viewed(request):
    """A view that renders the cart contents page"""
    return render(request, "viewed.html")


def add_to_viewed(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity=int(request.POST.get('quantity'))
    
    viewed = request.session.get('viewed', {})
    
    viewed[id] = viewed.get(id, quantity)
    
    request.session['viewed'] = viewed    
    return redirect(reverse('index'))


def adjust_viewed(request, id):
    """Adjust the quantity of the spefied product to the specified amount"""
    quantity=int(request.POST.get('quantity'))
    viewed = request.session.get('viewed', {})
    
    if quantity > 0:
        viewed[id] = quantity
    else:
        viewed.pop(id)
        
    request.session['viewed'] = viewed   
    return redirect(reverse('viewed'))