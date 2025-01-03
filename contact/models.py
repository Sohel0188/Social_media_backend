from django.db import models

# Create your models here.
class Contact_us(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contactFor = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.name} {self.email}'
    
    class Meta:
        verbose_name_plural = "Contact Us"