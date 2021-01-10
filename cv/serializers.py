# todo: add Basic CV serializer for just getting top level CV data
from rest_framework import serializers
from .models import CV, EducationEntry, ExperienceEntry, PersonalProject, Skill
from django.contrib.auth.models import User
from django_typomatic import ts_interface, generate_ts


@ts_interface()
class ReadEducationEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationEntry
        fields = "__all__"


@ts_interface()
class ReadExperienceEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceEntry
        fields = "__all__"


@ts_interface()
class ReadPersonalProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalProject
        fields = "__all__"


@ts_interface()
class ReadSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


@ts_interface()
class ReadCVSerializer(serializers.ModelSerializer):
    skills = ReadSkillsSerializer(many=True)
    experience_entries = ReadExperienceEntrySerializer(many=True)
    personal_project_entries = ReadPersonalProjectSerializer(many=True)
    education_entries = ReadEducationEntrySerializer(many=True)

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


@ts_interface()
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


@ts_interface()
class WriteSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["name"]


@ts_interface()
class WriteExperienceEntriesSerializer(serializers.ModelSerializer):
    cv = serializers.PrimaryKeyRelatedField(
        many=False, read_only=False, queryset=CV.objects.all()
    )

    class Meta:
        model = ExperienceEntry
        fields = "__all__"


@ts_interface()
class WritePersonalProjectsSerializer(serializers.ModelSerializer):
    cv = serializers.PrimaryKeyRelatedField(
        many=False, read_only=False, queryset=CV.objects.all()
    )

    class Meta:
        model = PersonalProject
        fields = "__all__"


@ts_interface()
class WriteEducationEntriesSerializer(serializers.ModelSerializer):
    cv = serializers.PrimaryKeyRelatedField(
        many=False, read_only=False, queryset=CV.objects.all()
    )

    class Meta:
        model = EducationEntry
        fields = "__all__"


# generate_ts("./generated-types/cv.ts")
