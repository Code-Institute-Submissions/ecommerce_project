from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentsForm
from django.utils import timezone


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

 
 
