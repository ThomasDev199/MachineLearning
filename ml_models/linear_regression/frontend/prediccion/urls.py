from django.urls import path
from . import views

urlpatterns = [
    path("", views.predecir, name="predecir"),
]