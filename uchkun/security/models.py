from django.db import models

class User(models.Model):
    ADMIN = 'admin'
    STUDENT = 'student'
    TEACHER = 'teacher'

    USER_TYPES = [
        (ADMIN, 'Admin'),
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    ]

    username = models.CharField(max_length=150, unique=True)  # Username
    password = models.CharField(max_length=255)  # Password (you should hash it)
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPES,
        default=STUDENT,
    )

    def __str__(self):
        return self.username
