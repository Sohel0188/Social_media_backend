from django.shortcuts import render
from . import serializer
from rest_framework import viewsets
from . import models
# Create your views here.
class postViewset(viewsets.ModelViewSet):
    queryset = models.CreatePost.objects.all()
    serializer_class = serializer.Postserializer
    
class storyViewset(viewsets.ModelViewSet):
    queryset = models.storyModel.objects.all()
    serializer_class = serializer.storySerializer
    
class commentsViewset(viewsets.ModelViewSet):
    queryset = models.commentModel.objects.all()
    serializer_class = serializer.commentSerializer
    
class reactionViewset(viewsets.ModelViewSet):
    queryset = models.reactionModel.objects.all()
    serializer_class = serializer.reactionSerializer