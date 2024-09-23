from django.db import models
from userAccount.models import UserAccount

# Create your models here.
class CreatePost(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='./files/images')
    video = models.FileField(upload_to='./files/videos')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='created_posts')
    
    def __str__(self):
        return f"{self.id}"
    
    
class storyModel(models.Model):
    image = models.ImageField(upload_to='./file/images/')
    created_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='story')
    def __str__(self):
        return f"{self.image}"
    
class commentModel(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='commenter')
    post = models.ForeignKey(CreatePost,on_delete=models.CASCADE)
    text = models.TextField()
    


CHOOSE_OPTION = [
    ( "👍", "👍"),
    ("😢", "😢",),
    ( "😆", "😆",),
]
class reactionModel(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='reacted_parson')
    post = models.ForeignKey(CreatePost,on_delete=models.CASCADE)
    reaction = models.CharField(max_length=25, choices=CHOOSE_OPTION)