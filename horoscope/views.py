from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}


def get_yyyy_converters(request, sign_zodiak):
    return HttpResponse(f'вы передали число из 4х цифр - {sign_zodiak}')


def get_my_float_converters(request, sign_zodiak):
    return HttpResponse(f'вы передали вещественное число - {sign_zodiak}')


def get_my_date_converters(request, sign_zodiak):
    return HttpResponse(f'вы передали дату - {sign_zodiak}')


def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope_name', args=[sign])
        li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a></li>"
    response = f"""
    <ol>
        {li_elements}
    </ol>
    """
    return HttpResponse(response)


@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'This is {self.name}, age - {self.age}'


def get_info_about_zodiak_sign(request, sign_zodiak: str):
    description = zodiac_dict.get(sign_zodiak)
    data = {
        'description': description,
        'sign': sign_zodiak,
        'my_class': Person('Will', 55)
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_zodiak_sign_by_number(request, sign_zodiak: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiak > len(zodiacs):
        return HttpResponseNotFound(f'неправильный порядок номера знака зодиака - {sign_zodiak}')
    name_zodiac = zodiacs[sign_zodiak - 1]
    redirect_url = reverse('horoscope_name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)
