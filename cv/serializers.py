# todo: add Basic CV serializer for just getting top level CV data
from rest_framework import serializers
from .models import CV, EducationEntry, ExperienceEntry, PersonalProject, Skill
from django.contrib.auth.models import User


class ReadEducationEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationEntry
        fields = "__all__"


class ReadExperienceEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceEntry
        fields = "__all__"


class ReadPersonalProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalProject
        fields = "__all__"


class ReadSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class ReadCVSerializer(serializers.ModelSerializer):
    skills = ReadSkillsSerializer(many=True)

    class Meta:
        model = CV
        fields = [field.name for field in model._meta.fields]
        fields.extend(
            [
                "education_entries",
                "experience_entries",
                "personal_project_entries",
                "skills",
            ]
        )


class WriteCVSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        many=False, read_only=False, queryset=User.objects.all()
    )

    class Meta:
        model = CV
        fields = [
            "user",
            "name",
            "position",
            "bio",
            "location",
            "email",
            "phone",
            "homepage_url",
            "linkedin_url",
        ]


class WriteSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["name"]
