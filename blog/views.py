from django.shortcuts import render

from .models import BlogPost, Category


# Create your views here.

def index(request):
    list_articles = BlogPost.objects.all()
    context ={"list_articles":list_articles}
    return render(request ,'index.html',context)

def detail(request, id_article):
    articles = BlogPost.objects.get(id=id_article)
    category = articles.category
    article_en_relations = BlogPost.objects.filter(category=category)
    context = {"articles": articles, "aer": article_en_relations}
    return render(request ,'detail.html',context)