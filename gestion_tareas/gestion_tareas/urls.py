from django.contrib import admin
from django.urls import path, include

from apps.tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),

    # INCLUDE app 'tasks'
    path('tasks/', include('apps.tasks.urls')),

]
