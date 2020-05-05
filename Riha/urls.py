from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('idcomplete/',include('idcomplete.urls')),
    path('', include('account.urls')),
]
