from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from myapp.views import *
from shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    # path('',views.index,name='home'),
]
handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
