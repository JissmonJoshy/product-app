from django.db import models

# Create your models here.
class Product(models.Model):
    pro_name=models.CharField(max_length=30,null=True)
    pro_price=models.IntegerField(null=True)
    pro_quantity=models.IntegerField(null=True)
    pro_image=models.ImageField(upload_to='image/',null=True)