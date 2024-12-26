from django.urls import path

from .import views

app_name='Article'

urlpatterns = [
    path('',views.ArticleList.as_view(),name='home_page'),
    path('page/<int:page>',views.ArticleList.as_view(),name='home_page'),
    path('Article/<slug:slug>',views.Article_detail,name='Article_detail'),
    path('Article/catagory/<slug:slug>',views.Show_articles_by_Catagory,name='Show_articles_by_Catagory'),
    path('Article/catagory/<slug:slug>/page/<int:page>',views.Show_articles_by_Catagory,name='Show_articles_by_Catagory'),
]
