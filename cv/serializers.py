# todo: add Basic CV serializer for just getting top level CV data
from rest_framework import serializers
from .models import CV


class ReadCVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = "__all__"


class WriteCVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = [field.name for field in model._meta.fields]
        fields.remove("id")
