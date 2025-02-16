from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)  # Название задачи
    description = models.TextField()  # Описание задачи
    deadline = models.DateTimeField()  # Дедлайн задачи
    is_completed = models.BooleanField(default=False)  # Статус выполнения задачи

    def __str__(self):
        return self.title  
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        
