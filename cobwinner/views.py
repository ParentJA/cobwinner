from django.shortcuts import HttpResponse
from django.shortcuts import render


def landing(request, code=''):
    code_state = code[:2]
    code_branch = code[2:4]
    code_type = code[4:]

    return render(request, 'landing.html', {

    })


def prizes(request):
    return render(request, 'prizes.html', {

    })