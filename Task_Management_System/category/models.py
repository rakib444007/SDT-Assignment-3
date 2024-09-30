from django.db import models

# Create your models here.

class Category(models.Model):
    CategoryName = models.CharField(max_length=110)
  
   

    def __str__(self) -> str:
        return self.CategoryName
