from django.shortcuts import render,get_object_or_404

from .models import Article,Catagory

# Create your views here.

def home_page(request):
    context={
        'Article':Article.objects.published(),
        'Last_slider':Article.objects.all()[:1]
    }
    return render(request,'home_page.html',context)

def Article_detail(request,slug):
    context={
        'object':get_object_or_404(Article.objects.published(),slug=slug)
    }
    return render(request,'Articles/Article_detail.html',context)

def Show_articles_by_Catagory(request,slug):
    context={
        'Catagory':get_object_or_404(Catagory,slug=slug,status=True)
    }
    return render(request,'Articles/Show_articles_by_Catagory.html',context)