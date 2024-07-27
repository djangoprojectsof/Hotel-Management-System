"""
URL configuration for hotel project.

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
from django.contrib import admin
from django.urls import path, include
from reservation import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('rooms', views.RoomViewSet,basename='rooms')
router.register('prices', views.PriceListViewSet,basename='prices')
router.register('bookings',views.BookingViewSet,basename='bookings')
router.register('users', views.UserViewSet,basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    #path('/', include('reservation.urls')),  # Include the URLs from the reservations app
    path('',views.home),

    path('create_room/', views.create_room, name='create_room'),
    path('book_room/', views.book_room, name='book_room'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_room_price/', views.add_room_price, name='add_room_price'),
    path('view_bookings/', views.view_booking, name='view_bookings'),
    path('users/', views.list_users, name='user_list'),
    path('rooms/', views.list_rooms, name='room_list'),
    path('room_prices/', views.list_room_prices, name='room_price_list'),

]
