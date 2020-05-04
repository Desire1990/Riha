from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required



from django.conf.urls import url
from .views import home_view

urlpatterns = [
    path('<int:pk>', home_view, name="home"),
    path('new/', views.createIdc, name='createIdc'),
    # path('profile/', views.person, name='person'),
    # path('signup/', signup_view, name="signup"),
    # path('sent/', activation_sent_view, name="activation_sent"),
    # path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]
