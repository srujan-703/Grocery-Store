from django.contrib import admin
from .models import item
from .models import category

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']
    
class AdminCategory(admin.ModelAdmin):
    list_display=['name']
    

# Register your models here.
admin.site.register(item, AdminProduct)
admin.site.register(category,AdminCategory)
