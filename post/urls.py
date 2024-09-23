from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# router.register(r'create', views.postViewset, basename='snippet'),
router.register('post', views.postViewset)
router.register('story', views.storyViewset)
router.register('react', views.reactionViewset)
router.register('comment', views.commentsViewset)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]