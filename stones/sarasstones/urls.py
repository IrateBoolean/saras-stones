from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:mineral_id>/', views.detail, name='detail'),
    path('<int:mineral_id>/checkout/', views.checkout, name='checkout'),
]