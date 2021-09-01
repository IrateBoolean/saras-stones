from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:mineral_id>/', views.detail, name='detail'),
    path('<int:mineral_id>/checkout/', views.checkout, name='checkout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)