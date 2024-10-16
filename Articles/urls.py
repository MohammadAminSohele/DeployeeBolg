from django.urls import path

from .import views

app_name='Article'

urlpatterns = [
    path('<slug:slug>',views.Article_detail,name='Article_detail'),
]
