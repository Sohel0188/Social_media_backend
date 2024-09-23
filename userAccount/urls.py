from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# router.register('register/', views.userRegistrationView , basename='user-registration')
router.register('list/', views.allUserViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.userRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
]