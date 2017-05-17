"""eboutique URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# eboutique/urls.py

from django.conf.urls import  include, url
from django.contrib import admin
from rest_framework import routers
from eboutique.views import *

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'supplier', SupplierViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'eboutique.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
  #   url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]
