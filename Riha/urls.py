from django.contrib import admin
from django.urls import path, include
# from settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('idcomplete/',include('idcomplete.urls')),
    path('', include('account.urls')),
]

# if DEBUG:
# 	urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
# 	urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
