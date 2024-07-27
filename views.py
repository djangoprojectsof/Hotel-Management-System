from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Room, PriceList, Booking, User
from .serializers import RoomSerializer, PriceListSerializer, BookingSerializer, UserSerializer
from .forms import RoomForm, PriceListForm, BookingForm, UserForm
from datetime import timedelta
from rest_framework.exceptions import ValidationError
#from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class PriceListViewSet(viewsets.ModelViewSet):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def list_users(request):
    users = User.objects.all()
    return render(request, 'templates/user_list.html', {'users': users})

def list_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'templates/room_list.html', {'rooms': rooms})

def list_room_prices(request):
    prices = PriceList.objects.all()
    return render(request, 'templates/room_price_list.html', {'prices': prices})


def home(request):
    return render(request,'templates/home.html')

def create_room(request):
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form=RoomForm()
    return render(request,'templates/create_room.html',{'form':form})

def book_room(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            booking=form.save(commit=False)
            #check room availability
            conflicting_bookings=Booking.objects.filter(
                room=booking.room,
                start_date__lt=booking.end_date,
                end_date__gt=booking.start_date
            )
            if not conflicting_bookings:
                booking.calculate_total_price()
                booking.save()
                return redirect('view_bookings')
            else:
                form.add_error(None,'This room is already booked for selected dates')
           # booking.total_price=calculate_price(booking.room,booking.start_date,booking.end_date)
           # booking.save()
            #return redirect('view_bookings')

    else:
        form=BookingForm()
        users = User.objects.all()
        rooms = Room.objects.all()
    return render(request,'templates/book_room.html',{'form':form,'users': users, 'rooms': rooms})

def add_user(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form=UserForm()
    return render(request,'templates/add_user.html',{'form':form})

def add_room_price(request):
    if request.method=='POST':
        form=PriceListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_price_list')
    else:
        form=PriceListForm()
        rooms = Room.objects.all()
    return render(request,'templates/add_room_price.html',{'form':form, 'rooms': rooms})

def view_booking(request):
    bookings=Booking.objects.all()
    return render(request, 'templates/booking_list.html',{'bookings':bookings})

#def calculate_price(room,start_date,end_date):
#    total_price=0
#    current_date=start_date
#    while current_date <= end_date:
#        price=PriceList.objects.filter(room=room,date=current_date).first()
#        if price:
#            total_price=total_price + price.price
#        else:
#            total_price=total_price+ room.default_price
#        current_date += timedelta(days=1)
#    return total_price


