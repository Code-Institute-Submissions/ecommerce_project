from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentsForm, MakePaymentForm, NewsletterForm
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
import stripe

# Create your views here.
def getposts(request):
   posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
   return render(request, "blogposts.html", {'posts': posts})
   
    
def viewpost(request, id):
    this_post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(post=this_post)
    form = CommentsForm()
    return render(request, "viewpost.html", {'post': this_post, 'comments': comments, 'form': form})
    
def addcomment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentsForm(request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        # comment.published_date = timezone.now()
        comment.save()
        return redirect("viewpost", post_id)

 
stripe.api_key = settings.STRIPE_SECRET

def newsletter(request):
    if request.method=="POST":
        newsletter_form = NewsletterForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if newsletter_form.is_valid() and payment_form.is_valid():
            newsletter = newsletter_form.save(commit=False)
            newsletter.date = timezone.now()
            newsletter.save()

            try:
                customer = stripe.Charge.create(
                    amount= int(499),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        newsletter_form = NewsletterForm()

    return render(request, "newsletter.html", {'newsletter_form': newsletter_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE })

