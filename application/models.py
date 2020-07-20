from django.db import models
from django.conf import settings


def increment_application_number():
    last_application = Application.objects.all().order_by('id').last()
    if not last_application:
        return 'CMN0001'
    application_no = last_application.application_no
    application_int = int(application_no.split('CMN')[-1])
    new_application_int = application_int + 1
    new_application_no = 'CMN' + str(new_application_int)
    return new_application_no  

class Application(models.Model):  
    
    SECTORS = [
        ('ENTERTAINMENT', 'Entertainment'),
        ('HEALTHCARE', 'Healthcare'),
        ('SPORTS', 'Sports'),
        ('ENVIRONMENT', 'Environment'),
        ('ECONOMIC', 'Economic'),
    ]

    STATUS = [
        ('PENDING', 'Pending Approval'),
        ('APPROVED', 'Approved'),
        ('DENIED', 'Denied'),
        ('CANCELLED', 'Cancelled')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=128)
    project_description = models.CharField(max_length=1500)
    project_sector = models.CharField(max_length=32, choices=SECTORS)
    people_impacted = models.IntegerField()
    application_no = models.CharField(max_length=7, 
        default=increment_application_number, null=True, blank=True, editable=False)
    status = models.CharField(max_length=32, choices=STATUS, default='PENDING')
    application_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-application_no"]
        unique_together = [['user', 'application_no']]

    def __str__(self):
        return self.application_no
    
    def get_absolute_url(self):
        return reverse('application-detail', kwargs={'pk': self.pk})