from rest_framework import viewsets, views
from .serializers import ReadCVSerializer, WriteCVSerializer
from .models import CV
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


class MyCV(views.APIView):
    def get(self, request):
        user = request.user
        user_cvs = CV.objects.filter(user=user)
        serializer = ReadCVSerializer(user_cvs, many=True)
        return JsonResponse(serializer.data, status=200)

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
        print(cv)
        serializer = WriteCVSerializer(data=cv, many=False)
        # todo: serialize all entries
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
