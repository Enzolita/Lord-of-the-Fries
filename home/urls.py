from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('about/',),
]   