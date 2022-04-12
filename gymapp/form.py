from django import forms


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
