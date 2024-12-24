# tasks/models.py
from django.db import models

# tasks/models.py

class Task(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Study', 'Study'),
        ('Personal', 'Personal'),
    ]

    title = models.CharField(max_length=255)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

