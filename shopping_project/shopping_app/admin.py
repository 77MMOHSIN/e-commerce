from django.contrib import admin
from .models import( Customer,Product,Cart,Orderplace)
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.
# @admin.register(Category1)
# class CustomerModelAdmin(admin.ModelAdmin):
#     list_display=['id', 'user', 'Catname']
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','zipcode','state']
        
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discounted_price','description','brand','category','product_image']
    
@admin.register(Cart)
class cartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','Product','quantity']
    

@admin.register(Orderplace)
class OrderplaceModelAdmin(admin.ModelAdmin):
    list_display=['id','user','Customer','Product','quantity','ordered_date','status']
    def customer(self,obj):
      link=reverse("admin:shoppin_app_customer_change",args=[obj.customer.pk])
      return format_html('<a href=""></a>',link,obj.customer.name)
    
    