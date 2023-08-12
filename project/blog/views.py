from django.shortcuts import render
from .models import Post


# Create your views here.
def homepage(request):
    all_posts = Post.objects.all()
    context = {"all_posts": all_posts}
    return render(request, "blog/home.html", context)

def homepage2(request):
    all_posts = Post.objects.all()
    context = {"all_posts": all_posts}
    return render(request, "blog/index.html", context)