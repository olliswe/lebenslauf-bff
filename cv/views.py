from rest_framework import views
from rest_framework.response import Response

from .models import CV, CVSkill, Skill
from .serializers import (
    ReadCVSerializer,
    WriteCVSerializer,
    WriteSkillSerializer,
    WriteExperienceEntriesSerializer,
    WritePersonalProjectsSerializer,
    WriteEducationEntriesSerializer,
)


class MyCV(views.APIView):
    def get(self, request):
        user = request.user
        user_cvs = CV.objects.filter(user=user)
        serializer = ReadCVSerializer(user_cvs, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        user = request.user
        cv = request.data
        experience_entries = cv.pop("experience_entries", None)
        personal_project_entries = cv.pop("personal_project_entries", None)
        education_entries = cv.pop("education_entries", None)
        skills = cv.pop("skills", None)
        cv["user"] = user.pk
        cv_serializer = WriteCVSerializer(data=cv, many=False)
        # todo: serialize all entries
        if cv_serializer.is_valid():
            cv = cv_serializer.save()

            # Handle Skills
            skills_serializer = WriteSkillSerializer(data=skills, many=True)
            if skills_serializer.is_valid():
                validated_skills = skills_serializer.data
                for skill in validated_skills:
                    existing_skill = Skill.objects.filter(name=skill["name"]).first()
                    if existing_skill:
                        CVSkill.objects.create(cv=cv, skill=existing_skill)
                    else:
                        new_skill = Skill.objects.create(name=skill["name"])
                        CVSkill.objects.create(cv=cv, skill=new_skill)
            else:
                cv.delete()
                return Response(skills_serializer.errors, status=400)

            # Handle Experience Entries
            parsed_experience_entries = []
            for entry in experience_entries:
                entry["cv"] = cv.pk
                parsed_experience_entries.append(entry)
            experience_entries_serializer = WriteExperienceEntriesSerializer(
                data=parsed_experience_entries, many=True
            )
            if experience_entries_serializer.is_valid():
                experience_entries_serializer.save()
            else:
                cv.delete()
                return Response(experience_entries_serializer.errors, status=400)

            # Handle Personal Project Entries
            parsed_personal_projects = []
            for entry in personal_project_entries:
                entry["cv"] = cv.pk
                parsed_personal_projects.append(entry)
            personal_projects_serializer = WritePersonalProjectsSerializer(
                data=parsed_personal_projects, many=True
            )
            if personal_projects_serializer.is_valid():
                personal_projects_serializer.save()
            else:
                cv.delete()
                return Response(personal_projects_serializer.errors, status=400)

            # Handle Education Entries
            parsed_education_entries = []
            for entry in education_entries:
                entry["cv"] = cv.pk
                parsed_education_entries.append(entry)
            education_entries_serializer = WriteEducationEntriesSerializer(
                data=parsed_education_entries, many=True
            )
            if education_entries_serializer.is_valid():
                education_entries_serializer.save()
            else:
                cv.delete()
                return Response(education_entries_serializer.errors, status=400)

            read_cv_serializer = ReadCVSerializer(cv, many=False)
            return Response(read_cv_serializer.data, status=201)
        return Response(cv_serializer.errors, status=400)
