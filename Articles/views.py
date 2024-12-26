from django.shortcuts import render,get_object_or_404

from django.views.generic import ListView,DetailView

from .models import Article,Catagory,Site_settings

# Create your views here.
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
    
class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(),slug=slug)
    
class CatagoryList(ListView):
    paginate_by=3
    template_name='Articles/Show_articles_by_Catagory.html'
    def get_queryset(self):
        global catagory
        slug = self.kwargs.get('slug')
        catagory = get_object_or_404(Catagory.objects.active(),slug=slug,status=True)
        return catagory.articles.published()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Catagory"] = catagory
        context["Last_slider"] = Site_settings.objects.active()
        return context