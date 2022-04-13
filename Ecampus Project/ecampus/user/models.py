from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    
    phone_regex = RegexValidator(regex=r'^[6-9]{1}\d{9}', message="Phone number must be in 10 digit and starts from 6 to 9")
    phone_number = models.CharField(validators=[phone_regex],max_length=10, unique=True)

    address = models.TextField(max_length=500, blank=True)

    class Meta():
        db_table="User"

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'faculty1'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'student1'

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'parent1'

