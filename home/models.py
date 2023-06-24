from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class NewUser(AbstractUser):
    USER_TYPE_CHOICES = (
        
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('receptionist', 'receptionist'),
    )
   
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES, default='student')
    experience = models.CharField(max_length=300)
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    fee = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title