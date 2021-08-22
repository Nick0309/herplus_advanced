"""HerPlus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu/', views.show_menu, name ='show_menu'),
    path('detail/<int:meal_id>', views.detail, name='detail'),
    path('detail/<int:meal_id>/addcart/', views.addcart, name='addcart'),
    path('show_cart/', views.show_cart, name='show_cart'),
    path('delete/<int:add_id>', views.delete, name='delete'),
    path('update/<int:add_id>', views.update, name='update'),
    path('update/<int:add_id>/goupdate', views.goupdate, name='goupdate'),
    path('fill_info/', views.fill_info, name='fill_info'),
    path('confirm/', views.confirm, name='confirm'),
    path('search/', views.search, name='search'),
    path('check_order/<str:order_id>', views.check_order, name='check_order'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)