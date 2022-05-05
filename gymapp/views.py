from django.contrib.auth import logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from .models import Coaches, SportStyle, PriceList
from .form import ContactForm, GymManageForm, UpdateCoachesForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        coaches = Coaches.objects.all()
        menu = {"title": "Войти", "url": "login"}
        context["menu"] = menu
        context["coaches"] = coaches
        return context


class CoachPageView(ListView):
    model = Coaches
    template_name = "gymapp/coaches.html"


class CoachesDetailView(DetailView):
    model = Coaches
    fields = ("name", "coach_information")


class CoachesCreateView(CreateView):
    model = Coaches
    form_class = UpdateCoachesForm
    context = {"coach": Coaches.objects.all()}
    template_name = "gymapp/create.html"
    success_url = "/coaches"


class CoachesUpdateView(UpdateView):
    model = Coaches
    form_class = UpdateCoachesForm
    template_name = "gymapp/update.html"


class CoachesDeleteView(DeleteView):
    model = Coaches
    success_url = "/coaches"
    template_name = "gymapp/coach_delete.html"


class LoginManager(DataMixin, LoginView):
    form_class = GymManageForm
    template_name = "gymapp/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        m_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(m_def.items()))

    def get_success_url(self):
        return reverse_lazy("gym-coaches")


def home(request):
    return render(request, "gymapp/home.html")


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


def logout_manager(request):
    logout(request)
    return redirect("manage-login")


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
