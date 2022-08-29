from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include, re_path
from backend.myapp import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('car/<int:car_id>/',views.categories)
    path('cars/<slug:type>/', views.categories, name='cars'),
    re_path(r'archive/(?P<year>[0-9]{4})/', views.archive, name='archive'), #для регулярок
]
