from django.contrib import admin
from . import models 
# Register your models here.

admin.site.register(models.CreatePost)
admin.site.register(models.storyModel)
admin.site.register(models.reactionModel)
admin.site.register(models.commentModel)