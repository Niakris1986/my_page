from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.


def get_info_about_zodiak_sign(request, sign_zodiak):
    if sign_zodiak == 'leo':
        return HttpResponse('знак зодиака лев')
    elif sign_zodiak == 'scorp':
        return HttpResponse('знак зодиака скорпион')
    else:
        return HttpResponseNotFound('страница не найдена')
