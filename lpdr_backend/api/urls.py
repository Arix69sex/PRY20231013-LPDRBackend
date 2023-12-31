"""
URL configuration for lpdr_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.api.urls')),
    path('api/usersData/', include('usersData.api.urls')),
    path('api/licensePlates/', include('licensePlates.api.urls')),
    path('api/vehicles/', include('vehicles.api.urls')),
    path('api/owners/', include('owners.api.urls')),
    path('api/infractions/', include('infractions.api.urls')),
    path('api/mockService/', include('externalInfractions.api.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
