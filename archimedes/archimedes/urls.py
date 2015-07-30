"""archimedes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from archimedes.views import IndexView
from archimedes.views import AboutusView
from archimedes.views import SolutionsView
from archimedes.views import ProductsView
from archimedes.views import NewsView
from archimedes.views import ContactView



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about_us$', AboutusView.as_view(), name='about_us'),
    url(r'^solutions', SolutionsView.as_view(), name='solutions'),
    url(r'^products$', ProductsView.as_view(), name='products'),
    url(r'^news$', NewsView.as_view(), name='news'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url('^home$', IndexView.as_view(), name='home'),

    url('^.*$', IndexView.as_view(), name='index'),
]