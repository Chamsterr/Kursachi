from django.db import models


class Category(models.Model):
    name_c = models.CharField(max_length=20, db_index=True,
                              verbose_name='Название')

    def __str__(self):
        return self.name_c

    class Meta:
        verbose_name_plural = 'Категория'
        verbose_name = 'Категории'
        ordering = ['name_c']


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Названия')
    attribute_list = models.TextField(verbose_name='Характеристики')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField()
    image = models.ImageField(upload_to="image/")
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.PROTECT,
                                 verbose_name='Категория')

    class Meta:
        verbose_name_plural = 'Товар'
        verbose_name = 'Товары'
