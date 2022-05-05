from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="gym-home"),
    path("coaches", views.CoachPageView.as_view(), name="gym-coaches"),
    path("coaches/<int:pk>/", views.CoachesDetailView.as_view(), name="coach-detail"),
    path("coaches/<int:pk>/update", views.CoachesUpdateView.as_view(), name="coach-update"),
    path("coaches/<int:pk>/delete", views.CoachesDeleteView.as_view(), name="coach-delete"),
    path("coaches/create", views.CoachesCreateView.as_view(), name="coach-create"),
    path("price", views.price_list, name="gym-price"),
    path("crossfit", views.crossfit, name="gym-crossfit"),
    path("crossfit-start", views.crossfit_start, name="gym-crossfit-start"),
    path("weightlifting", views.weightlifting, name="gym-weightlifting"),
    path("login", views.LoginAuth.as_view(), name="auth-login"),
    path("logout", views.logout_auth, name="auth-logout"),
    path("contacts", views.contacts, name="gym-contacts"),
    path("thanks", views.thanks, name="gym-thanks"),
]


