from django.urls import path
from . import views


urlpatterns = [
    path("signup", views.SignUpView.as_view(), name="accounts-signup"),
    path("profile", views.profile, name="accounts-profile"),
]
