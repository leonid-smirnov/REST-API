from django.db import models


class Product(models.Model):

    title = models.TextField(
        verbose_name='Заголовок объявления',
        null=True,
        blank=True,
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        null=True,
        blank=True,
    )
    currency = models.TextField(
        verbose_name='Валюта',
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Описание объявления',
        null=True,
        blank=True,
    )

    url = models.URLField(
        verbose_name='Ссылка на объявление',
        unique=False,
        null=True,
        blank=True,
    )
    published_date = models.DateTimeField(
        verbose_name='Дата публикации',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'#{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
