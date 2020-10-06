# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from django_resized import ResizedImageField

from datetime import date
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.shortcuts import reverse

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    mobile_number = models.CharField(_('mobile number'), max_length=13, unique=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.mobile_number


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):

    SUBCOUNTY = [
        ('Mvita', 'Mvita'),
        ('Kisauni', 'Kisauni'),
        ('Nyali', 'Nyali'),
        ('Changamwe', 'Changamwe'),
        ('Jomvu', 'Jomvu'),
        ('Likoni', 'Likoni')
    ]

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(_('email address'), blank=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)
    id_number = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=32, choices=SUBCOUNTY, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    avatar = ResizedImageField(
        size=[128, 128], crop=['middle', 'center'], 
        upload_to=user_directory_path, blank=True, null=True)

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_age(self):
        '''
        Returns age of user based on date ofr birth
        '''
        today = date.today()
        born = self.birth_date
        if self.birth_date:
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     '''
    #     Sends an email to this User.
    #     '''
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

    full_name = property(get_full_name)
    age = property(get_age)

    def __str__(self):
        return self.user.mobile_number
    
    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()