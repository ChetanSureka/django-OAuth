from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registerform(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, help_text='',
                                widget=forms.TextInput(
                                    attrs={
                                        "type": "text",
                                        "placeholder": ("Enter Username"),
                                    }
                                ))
    email = forms.EmailField(required=True,
                            widget=forms.EmailInput(
                                attrs={
                                    "type": "email",
                                    "placeholder": ("Enter E-mail"),
                                }
                            ))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(
                                    attrs={
                                        "type": "password",
                                        "placeholder": ("Enter Password"),
                                    }
                                ),
                                error_messages={'msg':'Must include an uppercase letter, a lowercase letter and a symbol'})
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(
                                    attrs={
                                        "type": "password",
                                        "placeholder": ("Password Confirmation"),
                                    }
                                ),
                                error_messages={'msg':'Make sure you entered the same password as above. Passwords are case sensitive.'})

    class Meta:
        model = User # Changes the user model.(default)
        fields = ["username", "email", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, response):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user