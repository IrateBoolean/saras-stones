from django.shortcuts import get_object_or_404, render
from .models import Stone

# Create your views here.
def index(request):
    context = {
        'hello_world': 'Hello, World!',
        'numbers': [x for x in range(10)]
    }
    return render(request, 'index.html', context)


def detail(request, mineral_id):
    stone = get_object_or_404(Stone, pk=mineral_id)
    return render(request, 'detail.html', {'stone': stone})