from django.shortcuts import render, get_object_or_404
from .models import Posts

def index(request):
    
    context = {
        "posts": Posts.objects.all()
    }

    return render (request, "app/index.html", context)

def post(request, id_post):
    
    context = {
        "post": get_object_or_404(Posts, id=id_post)
    }
    
    return render(request, "app/posts.html", context)