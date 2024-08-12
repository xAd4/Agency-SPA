from django.urls import path
from . import views

urlpatterns = [
    path("200/", views.status_200.as_view(), name="status-200"),
]
