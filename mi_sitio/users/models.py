from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    nombres = models.CharField(max_length=200, blank = True, null = True)
    apellidos = models.CharField(max_length=200, blank = True, null = True)
    tipo_identidad = models.CharField(max_length=75, blank = True, null = True)
    numero_identidad = models.CharField(max_length=75, blank = True, null = True)
    telefono = models.CharField(max_length=75, blank = True, null = True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
