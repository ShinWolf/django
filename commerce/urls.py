from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('services', views.services, name='services'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('loggedin', views.loggedin, name='loggedin'),
    path('logout', views.logout_view, name='logout'),
    path('avis', views.avis, name='avis'),
    path('listAvis', views.listAvis, name='listAvis'),
] 