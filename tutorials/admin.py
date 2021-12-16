from django.contrib import admin
from tutorials.models import Tutorial
from django.contrib.admin import ModelAdmin


@admin.register(Tutorial)
class TutorialAdmin(ModelAdmin):
    list_display = ('id', 'title', 'description', 'published')
    fields = ('title', 'description', 'published')
