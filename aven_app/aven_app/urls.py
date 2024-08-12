"""
URL configuration for aven_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import settings
from registration import urls
from app import urls
from api import urls
from helpers import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # Registration
    path("accounts/", include("registration.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    # Models JSON
    path("api/", include("api.urls")),
    # Home Page
    path("", include("app.urls")),
    # Helpers Page
    path("status/", include("helpers.urls")),
]

# MEDIA CONFIG
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)