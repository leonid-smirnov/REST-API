from django.db import models
import datetime

class Tutorial(models.Model):
    id = models.AutoField  # Идентификатор строки
    title = models.CharField(max_length=70, blank=False, default='')  # Название
    description = models.CharField(max_length=200, blank=False, default='')  # Описание
    published = models.BooleanField(default=False)  # Опубликовано
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False,
                                      blank=False)  # Дата создания
    edited_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)  # Дата изменения

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tutorial'
        ordering = ("-created_at",)
        verbose_name = "Example table"
        verbose_name_plural = "Example table"
