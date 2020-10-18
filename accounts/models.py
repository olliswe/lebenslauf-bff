from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Subscription(models.Model):
    subscription_name = models.CharField("Subscription Name", max_length=100)


# CREATE PROFILE WHEN USER IS CREATED
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscription = models.ForeignKey(
        Subscription, on_delete=models.SET_NULL, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if not self.subscription:
            free_subscription = Subscription.objects.get(subscription_name="FREE")
            if free_subscription:
                self.subscription = free_subscription
        super(UserProfile, self).save(*args, **kwargs)


# Create your models here.