from django.shortcuts import render, redirect, reverse, get_object_or_404

def viewed(request):
    """A view that renders the cart contents page"""
    return render(request, "viewed.html")


def add_to_viewed(request, id):
    """Add a quantity of the specified product to the cart"""
    
    viewed = request.session.get('viewed', {})
    
    viewed[id] = viewed.get(id)
    
    request.session['viewed'] = viewed    
    return redirect(reverse('index'))


