from . import models
from rest_framework import serializers
from django.contrib.auth.models import User

class allUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.UserAccount
        fields = '__all__'
   
class userRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    date_of_birth = serializers.DateField()
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password','date_of_birth']
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        date_of_birth = self.validated_data['date_of_birth']
        # is_active = self.validated_data[is_active]
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        if password != password2:
            raise serializers.ValidationError({'error':'Password did not match'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': 'This mail already exist'})
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        account.set_password(password)
        account.is_active = False
        account.save()
        models.UserAccount.objects.create(
            user = account,
            date_of_birth = date_of_birth,
        )
        return account

class loginSerializers(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)