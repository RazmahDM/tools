from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



# model card tools.


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name='Категория')
    img = models.ImageField('Картинка')
    thumbnail = models.ImageField('Маленькая картинка')
    slug = models.SlugField(max_length=250, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_slug": self.slug})
    

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=1)
        

class Tool(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Не опубликовано'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=250, blank=False, verbose_name='Название')
    image = models.ImageField(upload_to='images')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='slug')
    description = models.TextField(blank=False, verbose_name='Описание')
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    oldPrice = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время измененния')
    published = models.BooleanField(choices=tuple(map(lambda x : (bool(x[0]), x[1]), Status.choices)), default=Status.DRAFT, verbose_name='Статус публикации')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='tools')
    is_new = models.BooleanField('Новинка?')
    is_actia = models.BooleanField('Акция?')
    objects = models.Manager()
    is_published = PublishedManager()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Категория')

    def __str__(self):
        return f'Инструмент: {self.title}'
    
    class Meta: 
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]

    def get_absolute_url(self):
        return reverse('tool', kwargs={'tool_slug': self.slug})
    


class CartTool(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_slug": self.slug})
    


'''
class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name='Категория')
    slug = models.CharField(max_length=250, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
'''

# class Parts(models.Model):
    #class Status(models.IntegerChoices):
       # DRAFT = 0, 'Не опубликовано'
        #PUBLISHED = 1, 'Опубликовано'

   # title = models.CharField(max_length=250, blank=False, verbose_name='Название')
   # slug = models.SlugField(max_length=250, unique=True, verbose_name='slug')
   # description = models.TextField(blank=False, verbose_name='Описание')
   # price = models.DecimalField(default=0)
   # time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
   # time_update = models.DateTimeField(auto_now=True, verbose_name='Время измененния')
   # published = models.BooleanField(choices=tuple(map(lambda x : (bool(x[0]), x[1]), Status.choices)), default=Status.DRAFT, verbose_name='Статус публикации')
   # category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория товара')



  #  def __str__(self):
   #     return f'Запчасти/Расходники: {self.title}'
