from django.shortcuts import get_object_or_404, render
from .models import Post

def index(request):
    context = {
        "hi": "Hello World",
    }
    return render(request, "marketplace/index.html", context)



#usage of 404 page

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "marketplace/detail.html", {"post": post})

