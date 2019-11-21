from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return "{} - {}".format(self.name, self.event_id)

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
    class Meta:
        ordering = ["-event_id"]


class Session(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='sessions', null=False, blank=False)
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(blank=True,null=True  )
    end_date = models.DateTimeField(blank=True,null=True)
    speaker = models.CharField(max_length=200)
    session_id = models.AutoField(primary_key=True)
    
    def __str__(self):
       return self.name