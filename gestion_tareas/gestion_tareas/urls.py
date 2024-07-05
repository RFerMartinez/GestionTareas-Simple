from django.contrib import admin
from django.urls import path

from apps.tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.helloword),
]