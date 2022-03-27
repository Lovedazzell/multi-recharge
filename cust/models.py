from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userprofile(models.Model):
    name = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    mobile = models.IntegerField()
    status = models.CharField(max_length=100,default='I love Investments')
    profile_pic = models.ImageField(default='cust/images/profile.jpg')

class UserFunds(models.Model):
    name = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='funds')
    fd_owner = models.CharField(max_length=70 , null=True)
    address = models.CharField(max_length=300 ,null=True)
    email = models.EmailField(max_length=80,null=True)
    mobile = models.IntegerField()
    amount = models.IntegerField()
    order_id  = models.CharField(max_length=70,null=True)
    payment_id  = models.CharField(max_length=70,null=True)
    payment_status  = models.BooleanField(default=False)
    certificate_status = models.CharField(max_length=80,default='Regular')
    duration = models.CharField(max_length=70,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)







