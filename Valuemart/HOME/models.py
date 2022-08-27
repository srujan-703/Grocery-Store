from django.db import models

# Create your models here.
class item(models.Model):
    name = models.CharField(max_length=100)
    img =models.ImageField(upload_to='pics')
    price = models.IntegerField()
    category=models.ForeignKey('category',on_delete=models.CASCADE,default=1)
    
    @staticmethod
    def get_items_by_id(ids):
        return item.objects.filter(id__in=ids)
    
    @staticmethod
    def get_all_juices():
        return item.objects.filter(category=2)
    @staticmethod
    def get_all_vegetables():
        return item.objects.filter(category=1)
    @staticmethod
    def get_all_creams():
        return item.objects.filter(category=3)


class category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
