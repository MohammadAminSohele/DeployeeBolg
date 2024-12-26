from django.shortcuts import render,get_object_or_404

from django.core.paginator import Paginator
from django.views.generic import ListView

from .models import Article,Catagory,Site_settings

# Create your views here.

# def home_page(request,page=1):
#     Articles_list=Article.objects.published()
#     paginator=Paginator(Articles_list,3)
#     articles=paginator.get_page(page)
#     context={
#         'Article':articles,
#         'Last_slider':Article.objects.all()[:1]
#     }
#     return render(request,'home_page.html',context)

class ArticleList(ListView):
    paginate_by=3
    template_name='home_page.html'
    def get_queryset(self):
        global articles
        articles=Article.objects.published()
        return articles
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Article"] = articles
        context["Last_slider"] = Article.objects.all()[:1]
        return context
    
    

def Article_detail(request,slug):
    context={
        'object':get_object_or_404(Article.objects.published(),slug=slug)
    }
    return render(request,'Articles/Article_detail.html',context)

def Show_articles_by_Catagory(request,slug):
    context={
        'Catagory':get_object_or_404(Catagory,slug=slug,status=True),
        'Last_slider':Site_settings.objects.filter(status=True)
    }
    return render(request,'Articles/Show_articles_by_Catagory.html',context)