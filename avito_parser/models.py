from django.db import models


class Product(models.Model):

    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок объявления',
        null=True,
        blank=True,
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        null=True,
        blank=True,
    )

    room_number = models.CharField(
        max_length=15,
        verbose_name='Количество комнат',
        null=True,
        blank=True,
    )

    description = models.TextField(
        max_length=2000,
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
    published_date = models.TextField(
        verbose_name='Дата публикации',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'#{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
