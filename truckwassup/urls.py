"""truckwassup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static

import home.views
import account.views
import maps.views

urlpatterns = [
    path('', home.views.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('maps/', maps.views.home, name='maps'),
    path('detail/', home.views.detail, name='detail'),
    path('register/', home.views.register, name='register'),
    path('dev/', home.views.dev, name="dev"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
