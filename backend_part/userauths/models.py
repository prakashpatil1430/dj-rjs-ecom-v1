from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=60, null=True, blank=True)
    phone = models.CharField(max_length=60, null=True, blank=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    # if user not submiited full name we have to update dynamically from using
    # email field
    def save(self, *args, **kwargs):
        if not self.email or self.email.lower() == 'none':
            email_username = self.email.split('@')
            self.email = email_username[0] if email_username else ''

        if not self.username or self.username.lower() == 'none':
            self.username = self.email.split('@')[0] if self.email else ''

        super(User, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,  related_name='profile')

    # for here image field we are using Filefield because it can acces all formats
    # like jpg,gif,png we dont get error if we any format
    image = models.FileField(
        upload_to='image', default='default/default-user.jpg', null=True, blank=True)

    full_name = models.CharField(max_length=60, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=60, null=True, blank=True)
    country = models.CharField(max_length=60, null=True, blank=True)
    state = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    p_id = ShortUUIDField(unique=True, length=10, max_length=20,
                          prefix="236", alphabet="abcedefghijk")

    def __str__(self) -> str:
        if self.full_name:
            return str(self.full_name)
        else:
            return str(self.user.full_name)

    def save(self, *args, **kwargs):
        if not self.full_name or self.full_name.lower() == 'none':
            self.full_name = self.user.full_name

        super(Profile, self).save(*args, **kwargs)
