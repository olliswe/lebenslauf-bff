from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User


class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=100)
    position = models.CharField("Position", max_length=100)
    bio = models.TextField("Bio", max_length=20000)
    location = models.CharField("Location", max_length=200)
    email = models.CharField("Email", max_length=50)
    phone = models.CharField("Phone", max_length=30)
    homepage_url = models.CharField("Homepage URL", max_length=100)
    linkedin_url = models.CharField("LinkedIn URL", max_length=200)
    education_entries = JSONField()
    experience_entries = JSONField()
    personal_projects_entries = JSONField()
    skills = JSONField()

    def __str__(self):
        return self.name
