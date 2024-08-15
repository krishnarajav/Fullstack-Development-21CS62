from django.db import models

class Project(models.Model):
    student_name = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    language_used = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in months")

    def __str__(self):
        return f"{self.student_name} - {self.topic}"

