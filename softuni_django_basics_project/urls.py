"""
URL configuration for softuni_django_basics_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('movies/', include('movies.urls')),
    path('cast-and-crew/', include('people.urls')),
    path('studios/', include('studios.urls')),
]

# handler404 = 'common.views.custom_404_view'

if settings.DEBUG:  # or True for the static files to work if other options don't help me
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
