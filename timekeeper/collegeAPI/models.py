from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
class College(models.Model):
    college_ID = models.CharField(max_length=255, unique=True)
    college_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    website = models.URLField()
    year_founded = models.DateField()
    accreditation = models.DateField()
    building_ID_initial = models.CharField(max_length=255)
    user_ID_initial = models.CharField(max_length=255)
    def __str__(self):
        return (self.college_name.capitalize()+", "+(self.location).split(',')[0].capitalize()+", "+self.city.capitalize()+", "+self.country.capitalize()+", "+str(self.year_founded)[0:4])



class User(models.Model):
    user_id =models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    hometown_address = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_long_lat = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1)
    role = models.CharField(max_length=255)
    emergency_call = models.CharField(max_length=255)
    citizenship = models.ImageField(upload_to='citizenship_images/')
    profile_image = models.ImageField(upload_to='profile_images/')
    thumbnail = ImageSpecField(source='profile_image',
                               processors=[ResizeToFit(100, 100)],
                               format='JPEG',
                               options={'quality': 60})
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (str(self.user_id)+". "+self.email)