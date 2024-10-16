from django.urls import path

from .import views

urlpatterns = [
    path('<slug:slug>',views.Article_detail,name='Article_detail'),
]
