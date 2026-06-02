from django.contrib import admin
from .models import Cuisine, Category, MenuItem,Booking,Contact,Order,OrderItem

# Register your models here.

admin.site.register(Cuisine)
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderItem)