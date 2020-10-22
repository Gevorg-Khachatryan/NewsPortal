from django.urls import path
from .views import HomeView,NewsView,CategoriesView,NewsListView

urlpatterns = [
    path('',HomeView.as_view(),name='home-page'),
    path(r'^/categories/$',CategoriesView.as_view(),name='categories-page'),
    path(r'^/news/$',NewsListView.as_view(),name='news-page'),
    path(r'^/news/(?P<pk>[0-9]+)/$', NewsView.as_view(), name='content-page'),
    path(r'^/category/(?P<category>[0-9]+)/$', HomeView.view_by_category, name='view-by-category')
]
