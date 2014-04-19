from django.shortcuts import HttpResponse
from django.shortcuts import render

from prize.forms import PrizeRedemptionForm
from prize.forms import PrizeRetrievalForm

from prize.models import PrizeType


def prize_retrieval(request, code):
    if request.method == 'POST':
        form = PrizeRetrievalForm(request.POST)

        if form.is_valid():
            pass

    else:
        form = PrizeRetrievalForm()

    return render(request, 'prize/prize_retrieval.html', {
        'form': form
    })


def prize_redemption(request):
    if request.method == 'POST':
        form = PrizeRedemptionForm(request.POST)

        if form.is_valid():
            pass

    else:
        form = PrizeRedemptionForm()

    return render(request, 'prize/prize_redemption.html', {
        'form': form
    })


def prize_list(request):
    prize_types = PrizeType.objects.all()

    return render(request, 'prize/prize_list.html', {
        'prize_types': prize_types
    })


def prize_report(request):
    return render(request, 'prize/prize_report.html', {

    })