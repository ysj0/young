from django.db import models

# Create your models here.
class HelloWorld(models.Model): # Model을 상속 받는다
    text = models.CharField(max_length=255, null=False)