from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(_('username'), max_length=30, blank=False, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    second_name = models.CharField(_('second name'), max_length=30, blank=True)

    REQUIRED_FIELDS = ['first_name', 'second_name', 'email']


    def __str__(self):
        return self.email

class CustomUserAdmin(CustomUser):
    list_display = ('username', 'email', 'first_name', 'second_name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email', 'first_name', 'second_name')
    ordering = ('username',)

    class Meta:
        proxy = True
        verbose_name = 'user'
        verbose_name_plural = 'users'