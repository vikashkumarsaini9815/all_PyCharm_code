from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from ilp.models import User, Level, Challenge, Media
from ilp.serializers import UserSerializer, LevelSerializer, ChallengeSerializer, MediaSerializer
from django.core.exceptions import ObjectDoesNotExist
import sys
# Create your views here.
# GET data Level api

class User_level(APIView):
    def get (self, request):
        contact = request.query_params.get("contact")

        try:
            user = User.objects.get(contact=contact)
            level = Level.objects.filter(user=user)
            serializer_context = {'request': request, }
            serializer = LevelSerializer(level, context=serializer_context, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            response={"exception_type":exc_type.__name__,"filename": exc_tb.tb_frame.f_code.co_filename,"error_line_no":exc_tb.tb_lineno,"message":"No such user"}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)

# Get data Chalenge in level id

class Level_challenge(APIView):
    def get (self, request):
        id = request.query_params.get("id")
        try:
            level = Level.objects.get(id=id)
            challenge = Challenge.objects.filter(level=level)
            serializer_context = {'request': request, }
            serializer = ChallengeSerializer(challenge, context=serializer_context, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            response={"exception_type":exc_type.__name__,"filename": exc_tb.tb_frame.f_code.co_filename,"error_line_no":exc_tb.tb_lineno,"message":"No such user"}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)

# GET data media in level in

class Challenge_media(APIView):
    def get (self, request):
        id = request.query_params.get("id")
        try:
            level = Level.objects.get(id=id)
            challenge = Challenge.objects.filter(level=level)
            print("all challenge     ",challenge)
            media = Media.objects.filter(challenge=challenge)
            print("media vvvvvvvvvv",media)
            serializer_context = {'request': request, }
            serializer = MediaSerializer(media, context=serializer_context, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            response={"exception_type":exc_type.__name__,"filename": exc_tb.tb_frame.f_code.co_filename,"error_line_no":exc_tb.tb_lineno,"message":"No such user"}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)