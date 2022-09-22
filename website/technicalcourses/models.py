from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Allcourses(models.Model):
    coursename = models.CharField(max_length=200)
    insname = models.CharField(max_length=200)
    startFrom = models.DateTimeField('start from')

    def __str__(self):
        return self.coursename
        
    def was_recently_published(self):
        return self.startFrom >= timezone.now() - datetime.timedelta(days=1)    

class Details(models.Model):
    course = models.ForeignKey(Allcourses,on_delete=models.CASCADE)
    ct     = models.CharField(max_length=500)
    choice = models.BooleanField(default = False)

    def __str__(self):
        return self.ct        