from django.urls import path
from . import views


app_name = 'Info'
urlpatterns = [
    path('', views.index, name='index')]