from django.urls import path
from . import views

urlpatterns = [
    path('<sign_zodiak>', views.get_info_about_zodiak_sign),
]
