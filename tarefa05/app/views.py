from django.shortcuts import render
from .models import Posts

def index(request):
    
    posts = Posts.objects.all()
    
    context = {
        "posts": posts,
    }
    
    return render (request, "app/templates/index.html", context)

def post(request, id):
    
    postagem = get_object_or_404(Posts, id=id)
    
    context = {
        "post": postagem,
    }
    
    return render(request, "app/templates/posts.html", context)