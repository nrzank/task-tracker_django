from django.db import models


# Create your models here.
class Category(models):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


