from django.http import HttpResponse
from django.shortcuts import render
from .models import Couches, SportStyle, PriceList
from .form import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.views import generic


class CoachesListView(generic.ListView):
    model = Couches
    template_name = "gymapp/coaches.html"
    context_object_name = "coaches"


class CoachesDetailView(generic.DetailView):
    model = Couches


def home(request):
    return render(request, "gymapp/home.html")


def about_us(request):
    return render(request, "gymapp/about.html")


def thanks(request):
    return render(request, "gymapp/thanks.html")


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
            subject = "Test"
            body = {"name": form.cleaned_data["name"],
                    "email": form.cleaned_data["email"],
                    "message": form.cleaned_data["message"]}
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          settings.EMAIL_HOST_USER,
                          ["gaposhaa1987@gmail.com"]
                          )
            except BadHeaderError:
                return HttpResponse("Не корректный заголовок")
            return render(request, "gymapp/thanks.html")
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