from django.shortcuts import render, redirect
from rest_framework.views import APIView
from . import serializer
from . import models
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect

# Create your views here.

class allUserViewset(viewsets.ModelViewSet):
    queryset = models.UserAccount.objects.all()
    serializer_class = serializer.allUserSerializers


class userRegistrationView(APIView):

    serializer_class = serializer.userRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user.pk)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/user/active/{uid}/{token}"
            
            email_subject = "Confirm Your Email"
            email_body = render_to_string('email.html',{'confirm_link': confirm_link})
            email = EmailMultiAlternatives(email_subject,' ',to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("check Your mail for confirmation")
            # return Response({'uid': uid, 'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')

class UserLoginApiView(APIView):
  
    def post(self, request):
      
        serializers = serializer.loginSerializers(data=self.request.data)
       
        if serializers.is_valid():
            username = serializers.validated_data['username']
            password = serializers.validated_data['password']
            print(username)
            user = authenticate(username= username,password=password)
            if user:
                token,_ = Token.objects.get_or_create(user=user)
                user_account, create = models.UserAccount.objects.get_or_create(user=user)
                login (request,user)
                print(user_account.id)
                return Response({'token' : token.key, 'user_id': user_account.id})
                
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)