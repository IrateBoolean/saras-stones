from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponseRedirect
from .models import Borrow, Stone, User
from django.utils.datastructures import MultiValueDictKeyError
from django.utils import timezone


# Create your views here.
def index(request):
    stones = Stone.objects.all()
    users = User.objects.all()
    context = {
        'stones': stones,
        'users': users,
    }
    return render(request, 'index.html', context)


def detail(request, mineral_id):
    stone = get_object_or_404(Stone, pk=mineral_id)
    users = User.objects.all()
    context = {
        'stone': stone,
        'users': users,
    }
    return render(request, 'detail.html', context)


def checkout(request, mineral_id):
    stone = get_object_or_404(Stone, pk=mineral_id)
    try:
        borrower = User.objects.filter(name=request.POST['user'])[0]
    except MultiValueDictKeyError as e:
        borrower = False
    try:
        returned = request.POST['return']
    except MultiValueDictKeyError as e:
        returned = False
    if borrower:
        stone.checked_out = True
        stone.current_borrower = borrower
        transaction = Borrow(stone=stone, user=borrower, check_out=timezone.now())
        transaction.save()
        stone.save()
    else:
        transaction = Borrow.objects.filter(stone=stone, check_in=None)[0]
        transaction.check_in = timezone.now()
        transaction.save()
        stone.checked_out = False
        stone.current_borrower = None
        stone.save()
    context = {
        'stone': stone,
        'borrower': borrower,
        'returned': request,
    }
    return HttpResponseRedirect(reverse('detail', args=(stone.id,)))

    render(request, 'detail.html', context)
