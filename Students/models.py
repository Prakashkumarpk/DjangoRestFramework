from django.db import models

# Create your models here.

class Student(models.Model):

    # age=models.IntegerField(default=10)
    # weight = models.FloatField(null=1)
    # price = models.DecimalField(max_digits=10, decimal_places=2)

    # name = models.CharField(max_length=150)
    # feedback = models.TextField()

    # date_of_birth = models.DateField(auto_now=True)
    # date_of_birth_with_time = models.DateTimeField()
    # birth_time = models.TimeField()

    # is_admin = models.BooleanField()

    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Task(models.Model):

    student_ref = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    description = models.TextField()


class RankSheet(models.Model):

    tamil=models.IntegerField()
    english=models.IntegerField()
    maths=models.IntegerField()
    science=models.IntegerField()
    social_science=models.IntegerField()
    total=models.IntegerField()
    average=models.FloatField()
    result=models.BooleanField()