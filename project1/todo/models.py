from django.db import models

class Tarea(models.Model):
    TASK_STATUS_CHOICES = (
        ('To Do', 'To Do'),
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    )
    tarea = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=TASK_STATUS_CHOICES, default='To Do')

    def __str__(self):
        return self.tarea
