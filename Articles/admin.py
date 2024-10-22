from django.contrib import admin

from .import models

# Register your models here.

class CatagoryManager(admin.ModelAdmin):
    list_display=('title','position','id','parent')

admin.site.register(models.Article)
admin.site.register(models.Catagory,CatagoryManager)