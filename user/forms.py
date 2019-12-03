from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100, required=False)


class ProfileForm(forms.Form):
    username = forms.CharField(max_length=100)
    biography = forms.CharField(max_length=1000, required=False)
    email = forms.EmailField(max_length=100, required=False)
