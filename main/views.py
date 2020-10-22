from django.shortcuts import render
from django.views import generic, View
from .models import News,Categories
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

# Create your views here.
class HomeView(generic.ListView):
    model = News
    template_name='main/home.html'
    context_object_name = 'news'
    paginate_by = 10
    queryset = News.objects.all().order_by('-created_date')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        categories = Categories.objects.all()
        from_date = self.request.GET.get('from')
        to_date = self.request.GET.get('to')
        if from_date and to_date:
                context['news'] = News.objects.filter(created_date__range=(datetime.datetime.strptime(from_date, "%Y-%m-%d").date(),
                                                                           datetime.datetime.strptime(to_date, "%Y-%m-%d").date()))
        context['categories'] = categories
        return context

    @staticmethod
    def view_by_category(request, **kwargs):
        category_id = kwargs['category']

        page = request.GET.get('page', 1)
        from_date = request.GET.get('from')
        to_date = request.GET.get('to')
        if from_date and to_date:
            from_main = News.objects.filter(main_category__pk=category_id,
                created_date__range=(datetime.datetime.strptime(from_date, "%Y-%m-%d").date(),
                                     datetime.datetime.strptime(to_date, "%Y-%m-%d").date())).order_by('-created_date')
            from_other = News.objects.filter(other_category__pk=category_id,
                created_date__range=(datetime.datetime.strptime(from_date, "%Y-%m-%d").date(),
                                     datetime.datetime.strptime(to_date, "%Y-%m-%d").date())).order_by('-created_date')
        else:
            from_main = News.objects.filter(main_category__pk=category_id).order_by('-created_date')
            from_other = News.objects.filter(other_category__pk=category_id).order_by('-created_date')
        news = from_main | from_other
        categories = Categories.objects.all()
        news=news.distinct()
        paginator = Paginator(news, 10)
        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            news = paginator.page(1)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)
        context = {}
        context['news'] = news
        context['categories'] = categories
        context['selected_category_id'] = int(category_id)
        return render(request, 'main/home.html', context)

class NewsListView(generic.ListView):
    model = News
    template_name = 'main/news_page.html'
    context_object_name = 'news'
    paginate_by = 10
    queryset = News.objects.all().order_by('-created_date')

    def get_context_data(self,**kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        from_date = self.request.GET.get('from')
        to_date = self.request.GET.get('to',datetime.datetime.now())
        if from_date and to_date:
            news = News.objects.filter(created_date__range=(
                                            datetime.datetime.strptime(from_date, "%Y-%m-%d").date(),
                                            datetime.datetime.strptime(to_date, "%Y-%m-%d").date())).order_by(
                '-created_date')
            context['news'] = news
        return context



class CategoriesView(generic.ListView):
    model = News
    template_name = 'main/categories_page.html'
    context_object_name = 'categories'
    paginate_by = 10
    queryset = Categories.objects.all()



class NewsView(generic.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        news_id = kwargs['pk']
        news = News.objects.get(pk=news_id)
        context={}
        context['news'] = news
        return context

