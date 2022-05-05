from django import forms
from django.contrib.auth.forms import AuthenticationForm

from gymapp.models import Coaches


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={"placeholder": "Ваше имя", "class": "form_input",
                   }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
                attrs={"placeholder": "Ваш email",
                       "class": "form_input"}
                )
            )

    message = forms.CharField(
        min_length=5,
        widget=forms.Textarea(
            attrs={"placeholder": "Сообщение",
                   "class": "form_input",
                   "font color": "black"
                   }
        )
    )


class GymManageForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"placeholder": "Логин",
                                                                            "class": "form_input",
                                                                            "font color": "black"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"placeholder": "Пароль",
                                                                                 "class": "form_input",
                                                                                 "font color": "black"}))


class UpdateCoachesForm(forms.ModelForm):
    class Meta:
        model = Coaches
        fields = ["name", "coach_information"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form_input'})
        self.fields['coach_information'].widget.attrs.update({'class': 'form_input'})







