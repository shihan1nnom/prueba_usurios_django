from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'nombres', 'apellidos', 'tipo_identidad', 'numero_identidad', 'telefono')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'nombres', 'apellidos', 'tipo_identidad', 'numero_identidad', 'telefono')
