from django.contrib import admin
from .  models  import  userprofile  ,UserFunds

@admin.register(UserFunds)
class Adminuserdata(admin.ModelAdmin):
    list_display = ['payment_status','name','fd_owner','address','mobile','email','amount','order_id','payment_id','duration','date_created']

@admin.register(userprofile)
class Adminuserprofile (admin.ModelAdmin):
    list_display = ['name','mobile','profile_pic','status']