from django.db import models

# Create your models here.


class Class(models.Model):
    Class = models.IntegerField(default=0)

class Subject(models.Model):
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.subject}"

class Book(models.Model):
    Bkno = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=70)
    edition = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)




class School(models.Model):
    Sclid = models.IntegerField()
    udiseCode =  models.CharField(max_length=13)
    schoolName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.schoolName} ({self.udiseCode})"

class Teacher(models.Model):
    tid = models.IntegerField()
    uid = models.IntegerField(default = 0)
    name= models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="jobat", null=True)



    def __str__(self):
        return f"{self.name} ({self.uid})"



class Student(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=50)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    rollno = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="learnat")

    def __str__(self):
        return f"{self.name}, class: {self.Class}, Roll No.: {self.rollno}"
