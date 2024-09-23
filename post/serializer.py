from . import models
from rest_framework import serializers
from django.contrib.auth.models import User

class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreatePost
        fields = '__all__' 
        
class storySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.storyModel
        fields = '__all__'
        
class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.commentModel
        fields = '__all__'
    
class reactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.reactionModel
        fields = '__all__'