from django.db import models

# Create your models here.
class SuperHero(models.Model):
    name = models.CharField(max_length=200, default=0)
    cityOfOrigin = models.CharField(max_length=200, default=0)#textarea
    richOrSuperpower = models.CharField(max_length=200, default=0)#, choices=richSuperpower)
    whichSuperPower = models.CharField(max_length=200, default=0)#which superpowers
    superHeroRating= models.CharField(max_length=200, default=0)#rate
    abilities = models.CharField(max_length=200, default=0)#abilities textarea
