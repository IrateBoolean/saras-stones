from django.db import models
from django.utils import timezone
# Create your models here.

class Color(models.Model):
    color = models.CharField(max_length=32, null=False, unique=True)

    def __str__(self):
        return self.color

class Mineral(models.Model):
    mineral = models.CharField(max_length=100, null=False, unique=True)
    brief = models.CharField(max_length=200)
    properties = models.CharField(max_length=2000)

    def __str__(self):
        return self.mineral

class Cut(models.Model):
    cut = models.CharField(max_length=64, null=False, unique=True)

    def __str__(self):
        return self.cut

class Stone(models.Model):
    stone_name = models.CharField(max_length=200)
    stone_mineral = models.ForeignKey(Mineral, on_delete=models.PROTECT, null=False)
    stone_cut = models.ForeignKey(Cut, on_delete=models.PROTECT, null=False)
    stone_color = models.ForeignKey(Color, on_delete=models.PROTECT, null=False)
    notes = models.CharField(max_length=2000)
    img_path = models.CharField(max_length=100, unique=True)
    acquire_date = models.DateTimeField()
    checked_out = models.BooleanField(null=False)

    def __str__(self):
        return self.stone_name

