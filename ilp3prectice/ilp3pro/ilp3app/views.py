from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .models import *
from ilp3app.serializers import StudentsSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist




class AllinfoAPIView(APIView):

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        students = self.get_object(pk)
        serializer = StudentsSerializer(students,)
        return Response(serializer.data)