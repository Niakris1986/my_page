from django.urls import path
from . import views

urlpatterns = [
    path('<int:sign_zodiak>', views.get_info_about_zodiak_sign_by_number),
    path('<str:sign_zodiak>', views.get_info_about_zodiak_sign),
]
