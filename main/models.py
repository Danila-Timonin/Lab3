from django.db import models
from django.contrib.auth.models import  AbstractUser


class Course(models.Model):
    CATEGORY_CHOICES = [
        ('students', 'Студентам'),
        ('ege', 'Подготовка к ЕГЭ'),
    ]

    title = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField(blank=False, default='')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=False, default='students')
    image = models.ImageField(upload_to='course_images/', blank=False, default='')

    def __str__(self):
        return self.title


class Subscription(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_profile.username} - {self.course.title}"


class UserProfile(AbstractUser):
    can_edit_courses = models.BooleanField(default=False)
    subscriptions = models.ManyToManyField(Course, through=Subscription)

    def __str__(self):
        return self.username
