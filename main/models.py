from django.db import models

# Create your models here.
class News(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField(default=None, null=True, blank=True)
    main_category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    other_category = models.ManyToManyField('Categories',related_name='other_category', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Categories(models.Model):
    category_name = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.category_name

