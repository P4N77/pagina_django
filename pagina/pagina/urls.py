
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', views.blog, name ="blog"),
    path('contactanos/', views.contactanos, name ="contacto"),
    path('', views.index, name ="inicio"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('servicios/', views.servicios, name = "servicios"),
]
