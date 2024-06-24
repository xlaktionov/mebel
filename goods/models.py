from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(unique=True, max_length=255, verbose_name='Категория')
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True, verbose_name='URL')


    class Meta:
        db_table = "category"
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(unique=True, max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True, verbose_name='URL')
    descr = models.TextField(unique=True, blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(blank=True, null=True, default=0.00, max_digits=4, decimal_places=1, verbose_name='Цена')
    discount = models.DecimalField(blank=True, null=True, default=0.00, max_digits=4, decimal_places=1, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')



    class Meta:
        db_table = "product"
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def display__id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return self.price - self.price*self.discount/100

        return self.price



