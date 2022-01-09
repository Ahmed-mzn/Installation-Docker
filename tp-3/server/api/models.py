from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    qty = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    def get_created_at(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    def __str__(self):
        return self.name


    class Meta:
        ordering = ('id',)
