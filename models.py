from django.db import models
import datetime
class Room(models.Model):
    name = models.CharField(max_length=100)
    default_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class PriceList(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return  f"{self.room}-{self.date}-{self.price}"

class User(models.Model):
    username = models.CharField(max_length=100)
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.username

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking by {self.user} for {self.room}"

    def calculate_total_price(self):
        total = 0
        for single_date in (self.start_date + datetime.timedelta(n) for n in
                            range((self.end_date - self.start_date).days + 1)):
            daily_price = PriceList.objects.filter(room=self.room, date=single_date).first()
            if daily_price:
                total += min(daily_price.price, self.room.default_price)
            else:
                total += self.room.default_price
        self.total_price = total
        return total
