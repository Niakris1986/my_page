from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('<yyyy:sign_zodiak>', views.get_yyyy_converters),
    path('<my_date:sign_zodiak>', views.get_my_date_converters),
    path('<int:sign_zodiak>', views.get_info_about_zodiak_sign_by_number),
    path('<my_float:sign_zodiak>', views.get_my_float_converters),
    path('<str:sign_zodiak>', views.get_info_about_zodiak_sign, name='horoscope_name'),
]
