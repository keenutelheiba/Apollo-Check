from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# HOST MODEL
class Host(models.Model):
    host_name = models.CharField(max_length=50)
    host_email = models.EmailField(blank=True, null=True)
    host_phone = models.IntegerField()
    host_image = models.ImageField(upload_to='img/doctors')
    host_desc = models.CharField(max_length=50)
    address = models.CharField(max_length=100,default="HealthPlus, Rohini-22, New Delhi")
    status = models.BooleanField(default=True)
    available = models.CharField(max_length=50,default='')
    current_meeting_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + " : " + str(self.host_name)

# MEETING MODEL
class Meeting(models.Model):
    visitor_name = models.CharField(max_length=50)
    visitor_email = models.EmailField(blank=True, null=True)
    visitor_phone = models.IntegerField()
    host = models.CharField(max_length=50, default="")
    date = models.DateField(default=timezone.now)
    time_in = models.TimeField(default=timezone.now)
    time_out = models.TimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + ' : ' + str(self.visitor_name)

