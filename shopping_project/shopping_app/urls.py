from django.urls import path
from shopping_app import views
from django.conf import settings
from django.conf.urls.static import static  
from django.contrib.auth import views as auth_views
from .form import LoginForm,MYpassword
urlpatterns = [
    path('',views.Productview.as_view(),name='home'),
    # path('', views.home),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    # path('hj',views.base.as_view(),name='showcart' ),
    
    
    path('cart/',views.show_cart, name='showcart'),
    # plus function is defined
    path('pluscart/',views.plus_cart, name='cart'),
    path('minuscart/',views.minus_cart, name='cart'),
    path('removecart/',views.remove_cart, name='removecart'),
    
    path('buy/', views.buy_now, name='buy-now'),
    
    
    path('profile/',views.ProfileView.as_view(),
        name='profile'),
    
    
    
    path('address/', views.address, name='address'),
    
    path('orders/', views.orders, name='orders'),
    
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MYpassword,success_url='/passwordchangedone/'), name='changepassword'),
    
    
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='app/changedone.html'),name='passwordchange'),
    
     
    path('mobile/', views.mobile, name='mobile'),
    
    
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    
     
    # login process
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    # logout process
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    
    
    # regirstration process
    path('registration/', views.  customerregistrationview.as_view(), name='customerregistration'),
    
    # checkout function is run 
    path('checkout/', views.checkout, name='checkout'),
    # paymentdone function is run 
    path('paymentdone/', views.payment_done, name='paymentdone'),
    
    #Reset password processs 
   path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html'),name='password_reset') ,
    
    
    
   path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done') ,
   
   path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html'),name='password_reset_confirm'),
   
   
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html.html'),name='password_reset_complete '),
   
    
    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
