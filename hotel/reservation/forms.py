from django import forms
from .models import Room, PriceList, Booking, User

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'default_price']

class PriceListForm(forms.ModelForm):
    class Meta:
        model = PriceList
        fields = ['room', 'date', 'price']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'user', 'start_date', 'end_date']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'number']
