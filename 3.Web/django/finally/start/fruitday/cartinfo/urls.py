from django.conf.urls import url
from django.contrib import admin
from cartinfo import views
urlpatterns = [
    url('^addcart',views.add_cart,name="add_cart"),
    url('^cart',views.cart_info,name="cart"),
    url('^order',views.order,name="order"),
    url('^addorder',views.add_order,name="addorder"),
]