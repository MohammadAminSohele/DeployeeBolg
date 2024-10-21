from django.urls import path

from .import views

app_name='Article'

urlpatterns = [
    path('<slug:slug>',views.Article_detail,name='Article_detail'),
    path('catagory/<slug:slug>',views.Show_articles_by_Catagory,name='Show_articles_by_Catagory'),
    path('catagory/<slug:slug>/page/<int:page>',views.Show_articles_by_Catagory,name='Show_articles_by_Catagory'),
]
