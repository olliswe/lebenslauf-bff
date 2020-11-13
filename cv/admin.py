from django.contrib import admin
from .models import (
    CV,
    EducationEntry,
    ExperienceEntry,
    PersonalProject,
    Skill,
    PersonalProjectSkill,
    ExperienceEntrySkill,
    CVSkill,
)

admin.site.register(CV)
admin.site.register(EducationEntry)
admin.site.register(ExperienceEntry)
admin.site.register(PersonalProject)
admin.site.register(Skill)
admin.site.register(PersonalProjectSkill)
admin.site.register(ExperienceEntrySkill)
admin.site.register(CVSkill)


admin.site.site_header = "Lebenslauf"
