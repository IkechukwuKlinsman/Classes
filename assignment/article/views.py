from django.shortcuts import render
from .models import Article

# Create your views here.

def home(request):
    articles = Article.objects.all()
    context={"articles": articles}
    return render(request, "article/index.html", context)