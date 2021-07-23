from django.db import models


class NewModel (models.Model):
    text = models.CharField(max_length=255, null=False)