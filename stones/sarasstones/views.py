from django.shortcuts import get_object_or_404, render, reverse
from .models import Stone

# Create your views here.
def index(request):
    stones = Stone.objects.all()
    context = {
        'stones': stones
    }
    return render(request, 'index.html', context)


def detail(request, mineral_id):
    stone = get_object_or_404(Stone, pk=mineral_id)
    return render(request, 'detail.html', {'stone': stone})


def detail(request, mineral_id):
    stone = get_object_or_404(Stone, pk=mineral_id)
    return render(request, 'detail.html', {'stone': stone})
