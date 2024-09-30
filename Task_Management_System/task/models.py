from django.db import models
from category.models import Category
# Create your models here.

class TaskModel(models.Model):
    TaskTitle = models.CharField(max_length=100)
    TaskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    TaskAssingDate = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.TaskTitle


