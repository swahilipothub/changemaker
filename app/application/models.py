from django.db import models
from django.conf import settings


def increment_application_number():
    last_application = Application.objects.all().order_by('id').last()
    if not last_application:
        return 'CMN1001'
    application_no = last_application.application_no
    application_int = int(application_no.split('CMN')[-1])
    new_application_int = application_int + 1
    new_application_no = 'CMN' + str(new_application_int)
    return new_application_no  

class Application(models.Model):  
    
    SECTORS = [
        ('Technology', 'Technology and Innovation'),
        ('Art', 'Creativity and Art'),
        ('Healthcare', 'Promotion of Health'),
        ('Sports', 'Sports'),
        ('Environment', 'Environment'),
        ('Community', 'Community'),
    ]

    STATUS = [
        ('PENDING', 'Pending Approval'),
        ('APPROVED', 'Approved'),
        ('CANCELLED', 'Cancelled')
    ]

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    SUBCOUNTY = [
        ('Mvita', 'Mvita'),
        ('Kisauni', 'Kisauni'),
        ('Nyali', 'Nyali'),
        ('Changamwe', 'Changamwe'),
        ('Jomvu', 'Jomvu'),
        ('Likoni', 'Likoni')
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=13)
    id_number = models.CharField(max_length=10)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER)
    subcounty = models.CharField(max_length=32, choices=SUBCOUNTY)
    project_name = models.CharField(max_length=128)
    project_description = models.CharField(max_length=1500)
    project_sector = models.CharField(max_length=32, choices=SECTORS)
    people_impacted = models.IntegerField()
    application_no = models.CharField(max_length=7, 
        default=increment_application_number, null=True, blank=True, editable=False)
    status = models.CharField(max_length=32, choices=STATUS, default='PENDING')
    application_date = models.DateTimeField(auto_now_add=True)

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
    
    full_name = property(get_full_name)
    age = property(get_age)
    
    class Meta:
        ordering = ["-application_no"]
        unique_together = [['mobile_number', 'email', 'id_number', 'application_no']]

    def __str__(self):
        return self.application_no
    
    def get_absolute_url(self):
        return reverse('application-detail', kwargs={'pk': self.pk})