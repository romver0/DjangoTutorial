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
    path('addpage/', addpage, name='addpage'),
    path('post/<int:post_id>/', post, name='post'),
    path('filter/', filterViews, name='filter'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('category/<int:category_id>', show_category, name='category'),
]
