from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    storage_conditions = models.TextField()
    dosage = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="uploads")

    def __str__(self):
        return self.title
