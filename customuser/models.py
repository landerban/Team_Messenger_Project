from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, user_id=None, first_name=None, last_name=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if not user_id:
            raise ValueError("The User ID field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, user_id=user_id, **extra_fields)
        user.first_name = first_name
        user.last_name(last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, user_id=None, first_name=None, last_name=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, user_id=user_id, first_name=first_name, last_name=last_name, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=True, default="")
    user_id = models.CharField(max_length=20, unique=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'user_id'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']


class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name or self.email.split('@')[0]
