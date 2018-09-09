from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class City(models.Model):
    cityName = models.CharField(max_length=45)
    postalCode = models.IntegerField()
    coordinateLng = models.DecimalField(max_digits=12, decimal_places=10)
    coordinateLat = models.DecimalField(max_digits=12, decimal_places=10)

    def __str__(self):
        return self.cityName


# Interest table
class Interest(models.Model):
    interestName = models.CharField(max_length=35, unique=True)
     
    def __str__(self):
        return self.interestName


# Add more information to the user
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.OneToOneField(City, on_delete=models.DO_NOTHING, null=True)
    interestId = models.ManyToManyField(Interest, related_name="interestUser")
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()