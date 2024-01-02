# Sample views code
import requests
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class =LocationSerializer



def index(request):
    #Hint: Check your correct URL of your rest api

    response = requests.get('http://127.0.0.1:8000/api/Location/')
    print(response)
    locations = response.json()

    return render(request, 'index.html', {'locations': locations})
    pass



# class LocationListCreateView(generics.ListCreateAPIView):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer



