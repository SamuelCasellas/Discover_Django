from django.db import models

from django.utils import timezone

# Create your models here.

class ToDo(models.Model):
    todo_description = models.CharField(max_length=200)
    scheduled_time = models.DateTimeField() # Time for when the task is to be completed
    def over_due(self) -> bool:
        return timezone.now() > self.scheduled_time
    def __str__(self) -> str:
        return self.todo_description

class SingleInstruction(models.Model):
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE)
    instruction_step = models.TextField(max_length=250)
    step_number = models.IntegerField(default=0)
