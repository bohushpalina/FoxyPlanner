from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название события")
    description = models.TextField(verbose_name="Полное описание")
    published_date = models.DateTimeField(verbose_name="Дата публикации")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/events/{self.id}'
        
    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
    
