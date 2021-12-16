from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),    # Ссылка на админку
    url(r'^', include('tutorials.urls'))   # Ссылка на файл urls Tutorial
]
