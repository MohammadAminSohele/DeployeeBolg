from django.shortcuts import render,get_object_or_404

from .models import Article

# Create your views here.

def home_page(request):
    context={
        'Article':Article.objects.filter(status='p').order_by('created'),
        'Last_slider':Article.objects.order_by('-created').all()[:1]
    }
    return render(request,'home_page.html',context)

def Article_detail(request,slug):
    context={
        'object':get_object_or_404(Article,slug=slug,status='p')
    }
    return render(request,'Articles/Article_detail.html',context)