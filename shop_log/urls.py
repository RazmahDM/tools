"""
URL configuration for shop_log project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from shop_app import views
from django.urls import path
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('catalog/', views.catalog),
    path('rent_category/', views.rent),
    path('sale_product/', views.sale),
    path('buying/', views.buying),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('payment/', views.payment),
    path('tool/<slug:tool_slug>/', views.list_tool, name='tool'),
    path('catalog/<slug:category_slug>', views.list_category, name='category'),
    path('cart/', views.cart),
    path('add_to_cart/', views.add_to_cart),
    path('delete/<int:pk>', views.delete),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)