from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True) 

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    user_id = models.AutoField(db_column='user_id', primary_key=True) # กำหนด ID เอง
    username = models.CharField(db_column='username', max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    create_date = models.DateTimeField(db_column='create_date', auto_now_add=True)
    update_date = models.DateTimeField(db_column='update_date', auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        managed = True
        db_table = 'custom_user'
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
        ordering = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return self.is_superuser

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return self.is_superuser