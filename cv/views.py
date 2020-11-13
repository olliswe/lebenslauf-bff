from rest_framework import viewsets, views
from .serializers import ReadCVSerializer
from .models import CV
from rest_framework.response import Response


class MyCV(views.APIView):
    def get(self, request):
        user = request.user
        user_cvs = CV.objects.filter(user=user)
        serializer = ReadCVSerializer(user_cvs, many=True)
        return Response(serializer.data)
