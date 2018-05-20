from django.urls import path
from . import views

app_name = "app_djangoparser"

urlpatterns = [
    path('', views.index_page, name="index"),
]