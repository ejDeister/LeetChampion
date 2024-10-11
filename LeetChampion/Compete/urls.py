from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('lobby-<str:lobby-code>', views.lobby, name='lobby'),
    path('run', views.run, name='run'),
    path('submit', views.submit, name='submit'),
    path('results', views.results, name='results'),
]