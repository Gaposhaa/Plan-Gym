from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from accounts.form import ContactForm
from Plan_B import settings


class SignUpView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy("accounts-profile")
    template_name = "accounts/signup.html"

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(SignUpView, self).form_valid(form)


def profile(request):
    return render(request, "accounts/profile.html")


def price_booking(request):
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
        "accounts/price_booking.html",
        context=context,
    )
