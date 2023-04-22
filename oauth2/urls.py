from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from oauthapp import views

urlpatterns = [
    #...
    path('admin/', admin.site.urls),
    path('auth', views.auth),
    path('test', views.test,name="test")
]