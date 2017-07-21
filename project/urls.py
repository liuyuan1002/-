"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from taobao import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^hot$',views.hot),
    url(r'^kitchen',views.kitchen),
    url(r'^homeTextiles',views.home),
    url(r'^login$', views.login_view,name='login'),
    url(r'^logout', views.logout_view),
    url(r'^register$', views.register,name='register'),
    url(r'^goods/(?P<goods_id>\d+$)',views.goodsDetail,name='goodsDetail'),
    url(r'^admin/', admin.site.urls),
    url(r'^cart/$',views.cart),
    url(r'^search/(\w+)',views.search),
    url(r'^additem/(\d+)/(\d+)/$',views.add_to_cart,name='additem-url'),
    url(r'^removeitem/(\d+)/$',views.remove_from_cart,name='removeitem-url'),
]
