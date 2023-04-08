"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
from authApp.views import landingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landingPageView/', views.LandingPageView.as_view()),
    path('show-destinations/', landingPageView.show_destinations),
    path('show_articles/', landingPageView.show_articles),
    path('show_promotions/', landingPageView.show_promotions),
    path('show_opinions/', landingPageView.show_opinions),
    path('get_image/', landingPageView.get_image)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
