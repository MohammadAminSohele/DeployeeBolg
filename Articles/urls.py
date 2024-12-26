from django.urls import path

from .import views

app_name='Article'

urlpatterns = [
    path('',views.ArticleList.as_view(),name='home_page'),
    path('page/<int:page>',views.ArticleList.as_view(),name='home_page'),
    path('Article/<slug:slug>',views.ArticleDetail.as_view(),name='Article_detail'),
    path('Article/catagory/<slug:slug>',views.CatagoryList.as_view(),name='Show_articles_by_Catagory'),
    path('Article/catagory/<slug:slug>/page/<int:page>',views.CatagoryList.as_view(),name='Show_articles_by_Catagory'),
]
