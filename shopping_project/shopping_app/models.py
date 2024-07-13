from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinLengthValidator

# Create your models here.
STATE_CHOICES=((
    'KARACHI','KARACHI'
),('Bahalwalpur','Bahalwalpur'),('hasilpur','hasilpur'),('jamalpur','jamalpur'))
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=12)
    city=models.CharField(max_length=12)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=20)
    
    def __str__(self):
        return str(self.id)
    

CATEGORY_CHOICES=(('M','Moblie'),('L','Laptop'),('TW','Top Wear'),
                      ('BW','Bottom Wear'))

class Product(models.Model):
    title=models.CharField(max_length=23)
    selling_price=models.CharField(max_length=12)
    discounted_price=models.FloatField()
    description=models.TextField(max_length=200)
    brand=models.CharField(max_length=12)   
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image=models.ImageField(upload_to='productimage')
    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)   
    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.Product.discounted_price
    
     
STATUS_CHOICE=(('Accepted','Accepted'),
               ('packed','packed'),
('on the Way','on the way'),
('Delivered',"Delivered")  ,
('Cancel','cancel'))
class Orderplace(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
        Product=models.ForeignKey(Product,on_delete=models.CASCADE)
        quantity=models.PositiveIntegerField(default=1)
        ordered_date=models.DateTimeField(auto_now_add=True)
        status=models.CharField(max_length=50,choices=STATUS_CHOICE,default='pending')

        @property
        def total_cost(self):
         return self.quantity * self.Product.discounted_price 

# class Category1(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     Catname=models.CharField(max_length=200)
#     def __str__(self):
#         return str(self.id)
    



