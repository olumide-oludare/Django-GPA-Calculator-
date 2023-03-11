from django.db import models

class Grade(models.Model):
    course_code = models.CharField(max_length=255)
    credits = models.IntegerField()
    grade = models.FloatField()