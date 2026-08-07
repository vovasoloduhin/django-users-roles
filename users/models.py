from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('User', 'User'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100,
                            choices=ROLE_CHOICES,
                            default='User')

    def __str__(self):
        return f"{self.name} ({self.role})"