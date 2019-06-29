from django.db import models
from majors.models import Major

# Create your models here.
class Class(models.Model):
    title = models.CharField(max_length=200)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)