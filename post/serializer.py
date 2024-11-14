from . import models
from rest_framework import serializers
from django.contrib.auth.models import User

class Postserializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source = 'created_by.user.username', read_only=True)
    user_image = serializers.ImageField(source = 'created_by.profile_image', read_only=True)
    class Meta:
        model = models.CreatePost
        fields = ['id','description','image','video','created_at','user_name','user_image']
        
class storySerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='created_by.user.username', read_only=True)
    user_image = serializers.ImageField(source='created_by.profile_image', read_only=True)  # Assuming 'profile_image' field exists
    class Meta:
        model = models.storyModel
        # fields = '__all__'
        fields = ['id', 'image', 'user_name','user_image']
        
class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.commentModel
        fields = '__all__'
    
class reactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.reactionModel
        fields = '__all__'