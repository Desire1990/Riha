from django.urls import path
from . import views
from .views import home_view

urlpatterns = [
    path('<slug>', home_view, name="home"),
    path('new/', views.createIdc, name='createIdc'),
]
