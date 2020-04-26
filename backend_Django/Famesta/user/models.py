from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(_('email'), unique=True, blank=False)
    status = models.BooleanField(_('status'), default=False)

    def __str__(self):
        return self.username


def upload_user_profile_path(instance, filename):
    print("Coming to the Function")
    return "user_{0}/profile/{1}".format(instance.user.id, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    full_name = models.CharField(_('full_name'), max_length=200, null=True)
    mobile = models.IntegerField(_('mobile'), null=True)
    background_picture = models.ImageField(_('background_picture'), null=True, blank=True,
                                           upload_to=upload_user_profile_path)
    profile_picture = models.ImageField(_('profile_picture'), null=True, blank=True, upload_to=upload_user_profile_path)
    BioDescription = models.CharField(_('bio'), max_length=300, null=True, blank=True)
    date_of_birth = models.DateField(_('dob'), null=True, blank=True)
    gender_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(_('gender'), max_length=10, choices=gender_choice, null=True, blank=True)
    account_choice = (
        ('Public', 'Public'),
        ('Private', 'Private')
    )
    account_type = models.CharField(_('account_type'), max_length=50, choices=account_choice, default='Public')

    def __str__(self):
        return str(self.user.username) + " Profile"
