from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    #     labels = {'username': 'Nombre de usuario', 'email': 'Correo electrónico'}
    #     help_texts = {'username': 'Nombre de usuario', 'email': 'Correo electrónico'}
    #     error_messages = {'username': {'unique': 'El nombre de usuario ya existe'}, 'email': {'unique': 'El correo electrónico ya existe'}}
    #     widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}), 'email': forms.EmailInput(attrs={'class': 'form-control'})}
        
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user