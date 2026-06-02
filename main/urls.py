from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('menu/', views.menu),
    path('about/', views.about),
    path('contact/', views.contact),
    path('booking/', views.booking, name='booking'),
    path('order/<int:item_id>/',views.order_item,name='order_item'
),
]