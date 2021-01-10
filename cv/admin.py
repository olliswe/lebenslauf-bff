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


class ExperienceEntryInline(admin.StackedInline):
    model = ExperienceEntry
    extra = 0


class PersonalProjectInline(admin.StackedInline):
    model = PersonalProject
    extra = 0


class CVAdmin(admin.ModelAdmin):
    inlines = [ExperienceEntryInline, PersonalProjectInline]


admin.site.register(CV, CVAdmin)
admin.site.register(EducationEntry)
admin.site.register(ExperienceEntry)
admin.site.register(PersonalProject)
admin.site.register(Skill)
admin.site.register(PersonalProjectSkill)
admin.site.register(ExperienceEntrySkill)
admin.site.register(CVSkill)


admin.site.site_header = "Lebenslauf"
