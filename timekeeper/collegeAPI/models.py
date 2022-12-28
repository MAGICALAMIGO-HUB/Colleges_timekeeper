from django.db import models

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
