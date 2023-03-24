from rest_framework import serializers
from palpatine.models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude = []
        