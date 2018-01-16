from django.shortcuts import render, redirect, reverse, get_object_or_404

def viewed(request):
    return render(request, "viewed.html")


def add_to_viewed(request, id):

    viewed = request.session.get('viewed', {})
    
    viewed[id] = viewed.get(id)
    
    request.session['viewed'] = viewed    
    return redirect(reverse('index'))


