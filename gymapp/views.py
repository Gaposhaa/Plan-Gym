from django.http import HttpResponse
from django.shortcuts import render
from .models import Couches, SportStyle, PriceList
from .form import ContactForm
from django.core.mail import send_mail, BadHeaderError


def home(request):
    return render(request, "gymapp/home.html")


def about_us(request):
    return render(request, "gymapp/about.html")


def coaches(request):
    context = {
        "coaches": Couches.objects.all(),
    }
    return render(request, "gymapp/coaches.html", context)


def price_list(request):
    context = {
        "price_list": PriceList.objects.all(),
    }
    return render(request, "gymapp/price.html", context)


def crossfit(request):
    context = {
        "crossfit": SportStyle.objects.order_by("name")[0:1],
    }
    return render(request, "gymapp/crossfit.html", context)


def crossfit_start(request):
    context = {
        "crossfit_start": SportStyle.objects.order_by("name")[1:2],
    }
    return render(request, "gymapp/crossfit_start.html", context)


def weightlifting(request):
    context = {
        "weightlifting": SportStyle.objects.order_by("name")[2:],
    }
    return render(request, "gymapp/weightlifting.html", context)


def contacts(request):
    context = {}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data["name"], form.cleaned_data["email"], form.cleaned_data["message"])
    else:
        form = ContactForm()
    context["form"] = form
    return render(
        request,
        "gymapp/contacts.html",
        context=context,
    )


def send_message(name, email, message):
    pass
