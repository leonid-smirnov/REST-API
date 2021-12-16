from rest_framework import serializers
from tutorials.models import Tutorial

class TutorialSerializer(serializers.ModelSerializer):  # Сериалайзер для таблицы Туториал
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published',
                  'created_at',
                  'edited_at',
                  )
