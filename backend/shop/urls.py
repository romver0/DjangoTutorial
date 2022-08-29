
from django.contrib import admin
from django.urls import path,include

from backend.myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    # path('',views.index,name='home'),
]
handler404 = views.pageNotFound
