from . import views
from django.urls import path
from .views import Index
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('', Index.as_view(), name='home')
]   