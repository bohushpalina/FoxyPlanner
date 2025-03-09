from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)
    title = models.CharField(max_length=200)  # Название задачи
    description = models.TextField()  # Описание задачи
    deadline = models.DateTimeField()  # Дедлайн задачи
    is_completed = models.BooleanField(default=False)  # Статус выполнения задачи

    def __str__(self):
        return self.title  
    
    def get_absolute_url(self):
        return f'/tasks/'
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        
