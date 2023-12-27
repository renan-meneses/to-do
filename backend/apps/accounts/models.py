from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(
        self, username, email, password, is_superuser, **extra_fields
    ):
        now = timezone.now()
        if not username:
            raise ValueError(_("The given username must be set"))
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_superuser=is_superuser,
            last_login=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        user = self._create_user(
            username, email, password, False, **extra_fields
        )
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(_("username"), max_length=25)
    full_name = models.CharField(_("full name"), max_length=50)
    email = models.EmailField(_("email address"), max_length=95, unique=True)
    phone_number = models.CharField(max_length=14)
    updated_at = models.DateTimeField(_("updated at"), default=timezone.now)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "full_name", "phone_number"]

    objects = UserManager()
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        permissions = (
            ("list_users", "List users"),
            ("create_user", "Create user"),
            ("update_user", "Update user"),
            ("inactivate_user", "Inativa user"),
        )
    
    def __str__(self):
        return self.full_name

    def get_rules(self):
        return ", ".join([group.name for group in self.groups.all()])
