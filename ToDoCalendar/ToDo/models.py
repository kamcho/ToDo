from django.db import models
from datetime import datetime
# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=60)
    about=models.TextField(max_length=500)
    date=models.DateTimeField(auto_now=True)
    reminder=models.DateTimeField()
    status=models.CharField(max_length=10,default="Active")
    def expiry(self):
        if datetime.now().strftime('%Y:%m:%d:%H:%M:%S') > self.reminder.strftime('%Y:%m:%d:%H:%M:%S') :
            self.status="Expired"
        else:
            self.status="Active"

        return self.status

