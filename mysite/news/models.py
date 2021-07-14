from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент') #blank=True means empty str
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикаций') #auto_now_add=True means will be add created date and time
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено') #auto_now=True means updated_at will be add date and time when we will be change news
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True) #also for use ImageField need install Pillow
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория') # null=True was deleted, related_name='get_news'
    views = models.IntegerField(default=0)

    def get_absolute_url2(self):
        # return reverse('view_news', kwargs={'news_id': self.pk}) #param1 url name param1 param for url
        return reverse('view_news', kwargs={'pk': self.pk})  # param1 url name param1 param for url

    def my_func(self):
        return 'Hello from model News))'


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новость' # name
        verbose_name_plural = 'Новости' # names
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk}) #param1 url name param1 param for url


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Категория' # name
        verbose_name_plural = 'Категории' # names
        ordering = ['title']