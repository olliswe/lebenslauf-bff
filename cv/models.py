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
    homepage_url = models.TextField("Homepage URL", null=True, blank=True)
    linkedin_url = models.TextField("LinkedIn URL", null=True, blank=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    def __str__(self):
        return self.name

    @property
    def skills(self):
        return Skill.objects.filter(cvskill__cv__id=self.id)

    class Meta:
        ordering = ["-updated_at"]


class EducationEntry(models.Model):
    institution = models.TextField("Institution")
    degree = models.TextField("Degree")
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date", null=True, blank=True)
    description = models.TextField(
        "Description", max_length=20000, null=True, blank=True
    )
    current = models.BooleanField("Current", default=False)
    cv = models.ForeignKey(
        CV, on_delete=models.CASCADE, related_name="education_entries"
    )


class ExperienceEntry(models.Model):
    role = models.TextField("Role")
    company = models.TextField("Company")
    location = models.TextField("Location")
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date", null=True, blank=True)
    current = models.BooleanField("Current", default=False)
    description = models.TextField("Description", null=True, blank=True)
    cv = models.ForeignKey(
        CV, on_delete=models.CASCADE, related_name="experience_entries"
    )


class PersonalProject(models.Model):
    name = models.TextField("Name")
    description = models.TextField("Description", null=True, blank=True)
    start_date = models.DateField("Start Date", null=True, blank=True)
    end_date = models.DateField("End Date", null=True, blank=True)
    github_project_url = models.TextField("Github Project URL", null=True, blank=True)
    cv = models.ForeignKey(
        CV, on_delete=models.CASCADE, related_name="personal_project_entries"
    )


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
