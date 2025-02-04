from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password, allowed_ip):
        if not username:
            raise ValueError('Users must have username')
        if not password:
            raise ValueError('Users must have password')
        if not allowed_ip:
            raise ValueError('Users must have allowed_ip')

        user = self.model(username=username, allowed_ip=allowed_ip)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """This is a superuser with no IP restriction"""
        user = self.create_user(username, password, allowed_ip=None)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    allowed_ip = models.GenericIPAddressField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username