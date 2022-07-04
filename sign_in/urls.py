from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.sign_in, name="sign_in"),
    path('home', views.home, name="home"),
]
