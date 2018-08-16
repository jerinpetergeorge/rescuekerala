from rest_framework import serializers
from mainapp.models import Request


class RequestFetchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
