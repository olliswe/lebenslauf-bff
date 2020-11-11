from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User


class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Name")
    position = models.CharField("Position")
    bio = models.TextField("Bio", max_length=20000)
    location = models.CharField("Location")
    email = models.CharField("Email")
    phone = models.CharField("Phone")
    homepage_url = models.CharField("Homepage URL")
    linkedin_url = models.CharField("LinkedIn URL")

    def __str__(self):
        return self.name


class EducationEntry(models.Model):
    institution = models.CharField("Institution")
    degree = models.CharField("Degree")
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date", null=True, blank=True)
    description = models.TextField(
        "Description", max_length=20000, null=True, blank=True
    )
    current = models.BooleanField("Current", default=False)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)


class ExperienceEntry(models.Model):
    role = models.CharField("Role")
    company = models.CharField("Company")
    state_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")
    current = models.BooleanField("Current", default=False)
    github_project_url = models.CharField("Github Project URL", null=True, blank=True)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)


class PersonalProject(models.Model):
    name = models.CharField("Name")
    description = models.TextField(
        "Description", max_length=20000, null=True, blank=True
    )
    github_project_url = models.CharField("Github Project URL", null=True, blank=True)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)


class Skill(models.Model):
    name = models.CharField("Name")


class PersonalProjectSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    personal_project = models.ForeignKey(PersonalProject, on_delete=models.CASCADE)


class ExperienceEntrySkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    experience_entry = models.ForeignKey(ExperienceEntry, on_delete=models.CASCADE)


class CVSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)


## EducationJSON
"""
```
interface EducationJSON {
    institution:string;
    degree:string;
    start_year:integer;
    end_year?:integer;
    description?:string;
    current:boolean (default=false);
}
```


## ExperienceJSON

```
interface ExperienceJSON {
    role:string;
    company:string;
    start_month:integer;
    start_year:integer;
    end_month?:integer;
    current:boolean (default=false);
    tech_stack: string[];
    github_project_url?: string;
}
```



## PersonalProjectJSON


```.env
interface PersonalProjectJSON {
    name:string;
    description?:string;
    tech_stack: string[];
    github_project_url?: string;
}
```
"""
