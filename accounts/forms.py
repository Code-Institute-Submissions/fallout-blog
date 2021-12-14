from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    """
    Form for user login ability
    """
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'login_username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'password-user'}))


class RegisterForm(forms.ModelForm):
    """
    Registration form for new users
    """
    username = forms.CharField(
        label='Enter Username', min_length=6, help_text='Required')

    email = forms.EmailField(
        max_length=65, help_text='Required', error_messages={'required': 'We Need An Email!'})

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',)

    def clean_username(self):
        """
        Ensuring users have unique username when signing up
        """
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username Already Taken")
        return username

    def clean_password2(self):
        """
        Checking that the first and second password inputs match up
        """
        cleandata = self.cleaned_data
        if cleandata['password'] != cleandata['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cleandata['password2']

    def clean_email(self):
        """
        Ensuring the username is unique for the account
        """
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    def __init__(self, *args, **kwargs):
        """
        Styling to registration form
        """
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})
