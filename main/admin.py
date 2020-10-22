from django.contrib import admin
from .models import News,Categories


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass