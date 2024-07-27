from django.contrib import admin
from .models import Room,PriceList,User,Booking
# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id','name','default_price']
@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    list_display = ['id','room','date','price']
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','number']
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id','room','user','start_date','end_date','total_price']

