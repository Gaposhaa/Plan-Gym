from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="gym-home"),
    path("about_us", views.about_us, name="gym-about_us"),
    path("coaches", views.coaches, name="gym-coaches"),
    path("price", views.price_list, name="gym-price"),
    path("crossfit", views.crossfit, name="gym-crossfit"),
    path("crossfit-start", views.crossfit_start, name="gym-crossfit-start"),
    path("weightlifting", views.weightlifting, name="gym-weightlifting"),
    path("contacts", views.contacts, name="gym-contacts")
]

