from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)


