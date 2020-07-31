from django.contrib import admin
from .models import SMS, SMSTemplate, ATSettings

admin.site.register(SMS)
admin.site.register(SMSTemplate)
admin.site.register(ATSettings)