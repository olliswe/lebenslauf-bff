from django.db import models
from django.contrib.auth.models import User


class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField("Name")
    position = models.TextField("Position")
    bio = models.TextField("Bio")
    location = models.TextField("Location")
    email = models.TextField("Email")
    phone = models.TextField("Phone")
    homepage_url = models.TextField("Homepage URL")
    linkedin_url = models.TextField("LinkedIn URL")

    def __str__(self):
        return self.name


class EducationEntry(models.Model):
    institution = models.TextField("Institution")
    degree = models.TextField("Degree")
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date", null=True, blank=True)
    description = models.TextField(
        "Description", max_length=20000, null=True, blank=True
    )
    current = models.BooleanField("Current", default=False)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)


class ExperienceEntry(models.Model):
    role = models.TextField("Role")
    company = models.TextField("Company")
    state_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")
    current = models.BooleanField("Current", default=False)
    github_project_url = models.TextField("Github Project URL", null=True, blank=True)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)


class PersonalProject(models.Model):
    name = models.TextField("Name")
    description = models.TextField("Description", null=True, blank=True)
    github_project_url = models.TextField("Github Project URL", null=True, blank=True)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)


class Skill(models.Model):
    name = models.TextField("Name")


class PersonalProjectSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    personal_project = models.ForeignKey(PersonalProject, on_delete=models.CASCADE)


class ExperienceEntrySkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    experience_entry = models.ForeignKey(ExperienceEntry, on_delete=models.CASCADE)


class CVSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
