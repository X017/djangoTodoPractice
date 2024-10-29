from django.db import models
# Create your models here.

class todo_list(models.Model):
    title = models.CharField(max_length=256)
    body = models.CharField(max_length=256)
    finish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} :   {self.created_at}"
