from django.shortcuts import render

from .models import Article

# Create your views here.

def home_page(request):
    context={
        'Article':Article.objects.filter(status='p').order_by('created')
    }
    return render(request,'home_page.html',context)