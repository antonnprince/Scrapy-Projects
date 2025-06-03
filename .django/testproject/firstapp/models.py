from django.db import models

class MenuItems(models.Model):
    name = models.CharField(max_length=250, default='Unnamed Item')
    price = models.IntegerField(default=0)  

class Reservations(models.Model):
    first_name = models.CharField(max_length=255,default='Unnamed Item')
    last_name = models.CharField(max_length=255, default='Unnamed Item')
    guest_count = models.IntegerField(default=0)
    reservation_time = models.DateField(auto_now = True)
    comments = models.CharField(max_length=1000,default='Unnamed')   