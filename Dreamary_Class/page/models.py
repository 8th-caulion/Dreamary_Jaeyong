from django.db import models

# Create your models here.
class Designer(models.Model):
    Image=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=50)
    adress=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.name