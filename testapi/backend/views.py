from django.shortcuts import render,redirect
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from .serializers import HomeSerializer
from rest_framework.views import APIView
# Create your views here.
class home(generics.ListAPIView):
    serializer_class = HomeSerializer
    # we can change DailuPErformance to Performance or HourlyPerformance
    queryset = DailyPerformance.objects.filter_by_min_roi(0.2)
    
    