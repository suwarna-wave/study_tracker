from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    total_marks = models.IntegerField()

    def __str__(self):
        return self.name

class Unit(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    allocated_marks = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.subject.name})"

class Progress(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.unit.name} - {'Completed' if self.completed else 'Pending'}"