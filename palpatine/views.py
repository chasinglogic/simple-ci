from django.shortcuts import render
from rest_framework import viewsets
from palpatine.models import Job
from palpatine.serializers import JobSerializer
from django.db import transaction
from rest_framework.response import Response
from django.http import Http404

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def retrieve(self, request, pk=None):
        if pk != 'next':
            return super().retrieve(request, pk=pk)
        
        with transaction.atomic():
            job = Job.objects.filter(state=Job.State.WAITING).first()
            if not job:
                raise Http404
            job.state = Job.State.IN_PROGRESS
            job.save()

            return Response(self.get_serializer(job).data)


        return super().retrieve(request, pk=pk)
