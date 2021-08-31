from django.db import models
from django.utils import timezone
# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

class Mineral(models.Model):
    name = models.CharField(max_length=100, unique=True)
    brief = models.CharField(max_length=200, null=True)
    properties = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name

class Cut(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

class Stone(models.Model):
    name = models.CharField(max_length=200)
    mineral = models.ForeignKey(Mineral, on_delete=models.PROTECT)
    cut = models.ForeignKey(Cut, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    notes = models.CharField(max_length=2000, null=True)
    img_path = models.CharField(max_length=100, unique=True, null=True)
    acquire_date = models.DateTimeField()
    checked_out = models.BooleanField()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Borrow(models.Model):
    stone = models.ForeignKey(Stone, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    check_out = models.DateTimeField()
    check_in = models.DateTimeField(null=True, blank=True)