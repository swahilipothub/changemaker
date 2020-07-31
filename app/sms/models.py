from django.db import models
from django.conf import settings
from users.models import Profile

class ATSettings(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=128)
    api_key = models.CharField(max_length=128)
    sender = models.CharField(max_length=32)


class SMSTemplate(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    message = models.TextField()
    
    def __str__(self):
        return "%s" % self.name

class SMS(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    changemaker = models.ManyToManyField(Profile)
    message = models.TextField()
    number = models.CharField(max_length=13)
    status = models.CharField(max_length=50)
    messageId = models.CharField(max_length=256)
    cost = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'messages'

    def __str__(self):
        return "%s" % self.message
