from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include, re_path
# from backend.myapp import views
from myapp.views import *

urlpatterns = [
    path('', index, name='home'),
    # path('car/<int:car_id>/',views.categories)
    path('cars/<slug:type>/', categories, name='cars'),
    re_path(r'archive/(?P<year>[0-9]{4})/', archive, name='archive'),  # для регулярок
    path('about/', about, name='about'),
    path('post/', addPost, name='addPost'),
    path('filter/', filterViews, name='filter'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login')
]
