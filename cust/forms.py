from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField ,PasswordChangeForm , UserChangeForm
from django.contrib.auth.models import User
from . models import  userprofile ,UserFunds

# This class is for usercreation
class singupform(UserCreationForm):
    password1 = forms.CharField(label = 'Password',widget=forms.PasswordInput(attrs={'class':'edit-form','placeholder':'Password'}))
    password2 = forms.CharField(label = 'Password (again)',widget=forms.PasswordInput(attrs={'class':'edit-form','placeholder':'Password Confirm'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
            'username':forms.TextInput(attrs={'class':'edit-form','placeholder':'Usermane'}),
             'first_name':forms.TextInput(attrs={'class':'edit-form','placeholder':'First name'}),
              'last_name':forms.TextInput(attrs={'class':'edit-form','placeholder':'Last_name'}),
               'email':forms.EmailInput(attrs={'class':'edit-form','placeholder':'Email'})
        } 
        labels={
                'email':'Email'
        }


# User authentication form class 
class Loginform(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'edit-form','placeholder':'Password'}))
    username = UsernameField(widget = forms.TextInput(attrs={'class':'edit-form','placeholder':'Usermane'}))


# Class for Old password change
class Passwordform(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'edit-form','placeholder':'Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'edit-form','placeholder':'New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'edit-form','placeholder':'Confirm New Password'}))

# detail change panel for adminuser
class Userchangeform(UserChangeForm):
    password = None
    username = forms.CharField(label_suffix="",widget=forms.TextInput(attrs={'class':'edit-form'}))
    first_name = forms.CharField(label_suffix="",required=False,widget=forms.TextInput(attrs={'class':'edit-form'}))
    last_name = forms.CharField(label_suffix="", required=False,widget=forms.TextInput(attrs={'class':'edit-form'}))
    email = forms.EmailField(label_suffix="",widget=forms.EmailInput(attrs={'class':'edit-form'}))
    date_joined = forms.DateTimeField(label_suffix="",widget=forms.DateTimeInput(attrs={'class':'edit-form'}))
    last_login = forms.DateTimeField(label_suffix="" ,disabled=True,widget=forms.DateTimeInput(attrs={'class':'edit-form'}))
    class Meta:
        model =User
        fields = ['username','first_name','last_name','email','date_joined','last_login','groups']
        widgets = {
            'groups':forms.SelectMultiple(attrs={'class':'form-select w-25'})
        }


# detail change panel for nuser
class UserEditform(UserChangeForm):
    password = None
    username = forms.CharField(label_suffix="" ,widget=forms.TextInput(attrs={'class':'edit-form','placeholder':'Username'}))
    first_name = forms.CharField(label_suffix="",required=False,widget=forms.TextInput(attrs={'class':'edit-form','placeholder':'First name'}))
    last_name = forms.CharField(label_suffix="", required=False,widget=forms.TextInput(attrs={'class':'edit-form','placeholder':'Last name'}))
    email = forms.EmailField(label_suffix="",widget=forms.EmailInput(attrs={'class':'edit-form','placeholder':'name@example.com'}))
    last_login = forms.DateTimeField(label_suffix="", disabled=True,widget=forms.DateInput(attrs={'class':'edit-form'}))
    class Meta:
        model =User
        fields = ['username','first_name','last_name','email','last_login']
       

# DURATION = [
#     ('Select years','Select years'),
#     ('1 YEAR','1 YEAR'),
#     ('1.5 YEAR','1.5 YEAR'),
#     ('2 YEAR','2 YEAR'),
#     ('2.5 YEAR','2.5 YEAR'),
#     ('3 YEAR','3 YEAR'),
#     ('4 YEAR','4 YEAR'),
#     ('5 YEAR','5 YEAR'),
# ]

# class for fd details of User
class UserFdDataForm(forms.ModelForm):
    # duration = forms.ChoiceField(choices=DURATION,widget=forms.Select(attrs={'class':'form-select w-25'}))
    class Meta:
        model = UserFunds
        fields = '__all__'
        exclude=['name','order_id','payment_id','payment_status','duration',"certificate_status"]
        widgets ={
            'fd_owner':forms.TextInput(attrs={'class':'edit-form','placeholder':'Enter FD owner here'}),
            'address':forms.TextInput(attrs={'class':'edit-form','placeholder':'Enter your address here'}),
            'email':forms.EmailInput(attrs={'class':'edit-form','placeholder':' Emmail-address here'}),
            'mobile':forms.TextInput(attrs={'class':'edit-form','placeholder':'Enter without country code'}),
            'amount':forms.TextInput(attrs={'class':'edit-form','placeholder':'Amount of your FD'}),
        }
        
class profileform(forms.ModelForm):
    mobile =  forms.IntegerField(label_suffix="" ,widget=forms.TextInput(attrs={'class':'edit-form','placeholder':'mobile number'}))
    status =  forms.CharField(label_suffix="" ,widget=forms.TextInput(attrs={'class':'edit-form','placeholder':'Status'}))
    profile_pic = forms.ImageField(label_suffix="" ,widget=forms.FileInput(attrs={'class':'form-control w-50'}))
    class Meta:
        model = userprofile
        fields = '__all__'
        exclude = ['name']
        