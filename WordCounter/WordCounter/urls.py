from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='url_home'),
    path('count/', views.count, name='url_count'),
    path('about/', views.about, name='url_about')
]
