from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically generates an incrementing ID
    name = models.CharField(max_length=255)  # Student's name, maximum length of 255 characters
    university = models.CharField(max_length=100, unique=True)  # University ID, should be unique

    def __str__(self):
        return self.name

class Professor(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically generates an incrementing ID
    name = models.CharField(max_length=255)  # Professor's name, maximum length of 255 characters
    university = models.CharField(max_length=100, unique=True)  # University ID, should be unique

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically generates an incrementing ID
    name = models.CharField(max_length=255)  # Subject's name, maximum length of 255 characters
    professor = models.CharField(max_length=255)  # Foreign key to Professor model
    university = models.CharField(max_length=100, unique=True)  # University ID, should be unique
    type = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class RegisteredSubject(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically generates an incrementing ID
    student = models.CharField(max_length=255)  # Foreign key to Student model
    subject = models.CharField(max_length=255)  # Foreign key to Subject model
    grade = models.IntegerField()  # Grade, maximum length of 10 characters

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"