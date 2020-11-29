from rest_framework import views
from rest_framework.response import Response

from .models import CV, CVSkill, Skill
from .serializers import ReadCVSerializer, WriteCVSerializer, WriteSkillSerializer


class MyCV(views.APIView):
    def get(self, request):
        user = request.user
        user_cvs = CV.objects.filter(user=user)
        serializer = ReadCVSerializer(user_cvs, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        user = request.user
        cv = request.data
        experience_entries = cv.get("experience_entries")
        personal_project_entries = cv.get("personal_project_entries")
        education_entries = cv.get("education_entries")
        skills = cv.get("skills")
        for item in [
            "experience_entries",
            "personal_project_entries",
            "education_entries",
            "skills",
        ]:
            cv.pop(item, None)
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

            # Handle Personal Project Entries

            # Handle Education Entries

            return Response(cv_serializer.data, status=201)
        return Response(cv_serializer.errors, status=400)
