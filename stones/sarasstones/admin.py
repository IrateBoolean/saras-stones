from django.contrib import admin
from .models import Borrow, Color, Mineral, Cut, Stone, User
# Register your models here.
admin.site.register(Color)
admin.site.register(Mineral)
admin.site.register(Cut)
admin.site.register(Stone)
admin.site.register(User)
admin.site.register(Borrow)

