from django.db import models


# Create your models here.

class Category(models.Model):
    """
    Модель для категорий
        name - Наименование
        description - Описание
    """
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=255, verbose_name='Описание')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """
    Модель для продуктов:
        name - Наименование
        description - Описание
        image - Изображение (превью)
        category - Категория
        price - Цена за покупку
        created_at - Дата создания (записи в БД)
        updated_at - Дата последнего изменения (записи в БД)
        manufactured_at - Дата производства продукта
    """
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=255, verbose_name='Описание')
    image = models.ImageField(upload_to='product_image', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    manufactured_at = models.DateTimeField(
        auto_now=False,
        blank=True,
        null=True,
        verbose_name='Дата производства продукта'
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
