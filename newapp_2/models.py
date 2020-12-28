from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length = 60)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    added_date=models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

