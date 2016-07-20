from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Userprofile(models.Model):
    user=models.OneToOneField(User)
    Name = models.CharField(max_length=50)
    Address = models.TextField()
    Contact = models.CharField(max_length=10)
    image_url = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.user.username


class BackyardModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=6)
    size = models.IntegerField(default=0)
    rent = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)
    image_url1 = models.CharField(max_length=1000, blank=True)
    image_url2 = models.CharField(max_length=1000, blank=True)
    image_url3 = models.CharField(max_length=1000, blank=True)
    image_url4 = models.CharField(max_length=1000, blank=True)
    image_url5 = models.CharField(max_length=1000, blank=True)


