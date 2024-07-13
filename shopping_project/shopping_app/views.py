from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import View
from .form import CustomerRegistrationForm,Customerprofileform
from django.contrib import messages
from .models import Customer,Product,Cart,Orderplace
from django.db.models import Q
from django.http import JsonResponse
# class base view
from django.contrib.auth.decorators import login_required
#  function base view
from django.utils.decorators import method_decorator
class Productview(View):
    def get(self,request):
        totalitem=0
        topwears=Product.objects.filter(category='TW' )
        bottonwears=Product.objects.filter(category='BW' )
        mobile=Product.objects.filter(category='M' )
        if request.user.is_authenticated:
          totalitem=len(Cart.objects.filter(user=request.user))
        return render(request,'app/home.html',{'topwears':topwears,'bottonwears':bottonwears,'moblie':mobile,'totalitem':totalitem})

class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        alreadycart= False
        if request.user.is_authenticated:
            alreadycart=Cart.objects.filter(Q(Product=product.id)& Q(user=request.user)).exists()
        return render(request,'app/productdetail.html',{'product':product,'alreadycart':alreadycart})
        

# def product_detail(request):
#  return render(request, 'app/productdetail.html')
@login_required
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(user=user,Product=product).save()
    return redirect('/cart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        print(cart)
        amount=0.0
        shipping_amount=80.0
        total_amount=0.0
                 
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        print(cart_product)
        if cart_product :
            for p in cart_product:
                tempamount=(p.quantity*p.Product.discounted_price )
                amount += tempamount
                totalamount=amount+ shipping_amount
  
            return render(request, 'app/addtocart.html',{'cart':cart,'totalamount':totalamount,'amount':amount,'shipping_amount':shipping_amount})
    
        else:
            return render(request,'app/empty.html') 
        
        #  plus function run 
def plus_cart(request):
    if request.method=="GET":
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(Product=prod_id)& Q(user=request.user))
        c.quantity +=1
        c.save()
        amount=0.0
        shipping_amount=80.0 
        
                 
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
         tempamount=(p.quantity * p.Product.discounted_price )
         amount += tempamount
                
                 
        data = {
         'quantity':c.quantity,
         'amount':amount,
         'totalamount':amount+ shipping_amount
            } 
        return JsonResponse(data) 
              

       
 #  minus function run 
def minus_cart(request):
    if request.method=="GET":
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(Product=prod_id)& Q(user=request.user))
        c.quantity -=1
        c.save()
        amount=0.0
        shipping_amount=80.0 
        total_amount=0.0
                 
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
         tempamount=(p.quantity * p.Product.discounted_price )
         amount += tempamount
    
                
                 
        data = {
         'quantity':c.quantity,
         'amount':amount,
         'totalamount':amount+ shipping_amount
            } 
        return JsonResponse(data) 
  
# remove cart function is runs 
        
def remove_cart(request):
    if request.method=="GET":
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(Product=prod_id)& Q(user=request.user))
        c.delete()
        amount=0.0
        shipping_amount=80.0 
        total_amount=0.0
                 
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
         tempamount=(p.quantity * p.Product.discounted_price )
         amount += tempamount
        #  totalamount=amount + shipping_amount 
                
                 
        data = {
         'amount':amount,
         'totalamount':amount+ shipping_amount 
            } 
        return JsonResponse(data) 
            
        
 



def buy_now(request):
 return render(request, 'app/buynow.html')

@login_required
def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

@login_required
def orders(request):
    orderplace=Orderplace.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'orderplace':orderplace})

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    if data ==None:
        mobiles=Product.objects.filter( category='M')
    elif data=='infinitx' or data=='sumsung':
        mobiles=Product.objects.filter( category='M').filter(brand=data) 
    elif  data =='below':
        mobiles=Product.objects.filter( category='M').filter( discounted_price__lt=25000)
    elif  data =='above':
        mobiles=Product.objects.filter( category='M').filter( discounted_price__gt=2000)
    
        
               
    return render(request, 'app/mobile.html',{'mobiles':mobiles})

def login(request):
 return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class customerregistrationview(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html', {'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success (request,'registration is Submitted Successfully!!!!')
            form.save()
           
        return render(request,'app/customerregistration.html', {'form':form})
        
        
     
# checkout function is runs
@login_required
def checkout(request):
   totalamount=0.0
   user=request.user
   add=Customer.objects.filter(user=user) 
   cart_items=Cart.objects.filter(user=user)
   amount=0.0
   shipping_amount=80.00
#    totalamount=0.0
   cart_product=[p for p in Cart.objects.all() if p.user==request.user]
   if cart_product:
       
       for p in cart_product:
         tempamount=(p.quantity * p.Product.     discounted_price )
         amount += tempamount
         
         
         totalamount=amount+shipping_amount 
    
   return render(request, 'app/checkout.html',{'add':add,'totalamount':totalamount,'cart_items':cart_items})

@login_required
def payment_done(request):
    user=request.user
    custid=request.GET.get('custid')
    ustomer=Customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    for c in cart:
        Orderplace(user=user,Customer=ustomer,Product=c.Product,quantity=c.quantity).save()
        c.delete()
    return redirect("orders") 
        
    


# def profile(request):
#  return render(request, 'app/profile.html')
@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self, request):
        
        form=Customerprofileform()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        form=Customerprofileform(request.POST)
        if form.is_valid():
            usr=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            req=Customer(user=usr ,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            req.save()
            messages.success(request,'Congratulations!!profile update Successfully')
            
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})