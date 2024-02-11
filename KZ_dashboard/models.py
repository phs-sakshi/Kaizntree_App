from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=50)

class KZ_dashboard(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    stock_status = models.PositiveIntegerField()
    available_stock = models.PositiveIntegerField()
