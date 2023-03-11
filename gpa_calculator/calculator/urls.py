# calculator/urls.py
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views


# app_name = 'calculator'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_grade/', views.add_grade, name='add_grade'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)