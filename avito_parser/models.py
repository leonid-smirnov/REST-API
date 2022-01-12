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
    floor = models.IntegerField(
        verbose_name='Этаж квартиры',
        null=True,
        blank=True,
    )

    floors = models.CharField(
        max_length=5,
        verbose_name='Этажей в здании',
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
        unique=True,
        null=True,
        blank=True,
    )
    published_date = models.CharField(
        max_length=20,
        verbose_name='Дата публикации',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'#{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
