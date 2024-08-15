from django.db import models

class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    
    def __str__(self):
        return self.name    
    
class Course(models.Model):
    c_id = models.CharField(primary_key=True, max_length=10)
    c_name = models.CharField(max_length=50, default='')
    enrollment = models.ManyToManyField(Student, blank='True')
    
    def __str__(self):
        return self.c_name