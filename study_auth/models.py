from django.contrib.auth.hashers import make_password
from django.db import models
from django.forms import ValidationError


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["email"], name="unique_email")]

    def __str__(self):
        return self.email
