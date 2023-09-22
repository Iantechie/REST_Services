from django.db import models

# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    product = models.ForeignKey("Products", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Products(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    