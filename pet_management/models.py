from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=180)
    description = models.TextField()
    url = models.URLField(null=True)
    is_adopted = models.BooleanField(default=False)
