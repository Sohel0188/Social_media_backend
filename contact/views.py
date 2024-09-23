from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact_us.objects.all()
    serializer_class = serializers.ContactSerializer