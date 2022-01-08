from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    qty = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('id',)
