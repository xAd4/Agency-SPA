from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("property/gallery/<int:pk>", views.PropertyGalleryView.as_view(), name="property_gallery"),
    path("property/gallery/create/", views.PropertyGalleryCreateView.as_view(), name="property_gallery_create")
]
