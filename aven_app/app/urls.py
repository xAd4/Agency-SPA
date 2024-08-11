from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("property/gallery/", views.PropertyGalleryView.as_view(), name="property_gallery"),
]
