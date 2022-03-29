from django.shortcuts import render
from django.contrib import messages
from .forms import singupform , Loginform ,Passwordform , Userchangeform ,UserFdDataForm , UserEditform ,profileform
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth import authenticate, login , logout , update_session_auth_hash
from django.views import View
from . models import UserFunds
from . generater import render_to_pdf
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


# view for show the pdf 
class Viewpdf(View):
    def get(self, request,*args , **kwargs):
        data = {
            'hello':'hello',
            'harry':'harry'
        }
        pdf = render_to_pdf('cust/certificate.html',data)
        return HttpResponse(pdf ,content_type = 'application/pdf' )


# This is coustmer profile page
def profile(request):
    if request.user.is_authenticated:
        cf = UserFunds.objects.filter(name__username = request.user).values('payment_status')
        payment_status= False
        for i in range(len(cf)):
            for key, val in cf[i].items():
                if val == True:
                    payment_status = True
                    break
        context = {'active3':'active','payment_status':payment_status}
        return render(request,'cust/profile.html',context)
    else:
        return HttpResponseRedirect('/login/')


# tHE function for user login page 
def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = Loginform(request=request , data= request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname ,password = upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        else:
            form = Loginform()
        context = {'form':form}
        return render(request,'cust/login.html',context)
    else:
        return HttpResponseRedirect('/profile/')
        



# the function for user creation 
def usersingup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = singupform(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/login/')
        else:    
            form = singupform()
        context = {'form':form}
        return render(request,'cust/singup.html',context)
    else:
        return HttpResponseRedirect('/profile/')



# User logout function
def userlogout(request):
    if  request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')



# Change password with old password
def userpwdchange(request):
    if  request.user.is_authenticated:
        if request.method == 'POST':
            form = Passwordform(user = request.user , data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, request.user)
                return HttpResponseRedirect('/')
        else:
            form = Passwordform(user=request.user)
        context = {'form':form}
        return render(request,'cust/Password.html',context)
    else:
        return HttpResponseRedirect('/login/')



# Admin panel Function
def admindisplay(request):
    if  request.user.is_superuser == True:
        data = User.objects.all().count()
        amount = UserFunds.objects.values('amount').exclude(payment_status=False)
        pending = UserFunds.objects.filter(certificate_status='Pending').count()
        paid = User.objects.filter(funds__payment_status = True).count()
        grand_total  = 0
        for i in range(len(amount)):
            for key , val in amount[i].items():
                grand_total += int(val)
        
        context = {'data':data,'pdata':pending,'active1':'active','grand_total':grand_total,'paid':paid}
        return render(request,'cust/admin.html',context)  
    else:
        return HttpResponseRedirect('/profile/')


# this function shows all users data to admin
def allusers(request):
    if  request.user.is_superuser == True:
        data = User.objects.all()
        context = {'data':data,'active2':'active'}
        return render(request,'cust/alluser.html',context) 
    else:
        return HttpResponseRedirect('/profile/')


# admin panel for edit the details of user
def admin_user_edit(request,pk):
    if  request.user.is_superuser == True:
        udata = User.objects.get(pk = pk)
        if request.method == 'POST':
            form = Userchangeform(instance = udata, data = request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/allusers/')
        else:
            form = Userchangeform(instance = udata)
        return render(request,'cust/admin_edit.html',{'form':form})   
    else:
        return HttpResponseRedirect('/profile/')

        
# fd apply form page
def applyFd(request,pk):
    if request.method == 'POST':
        form = UserFdDataForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['fd_owner']
            uadd = form.cleaned_data['address']
            uemail = form.cleaned_data['email']
            uamount = form.cleaned_data['amount']
            uamo = int(form.cleaned_data['amount'] * 100)
            umob = form.cleaned_data['mobile']
            client =razorpay.Client(auth=('rzp_test_Vq2wtgCcPJuQaB','S78FPRPrEB8KPHQkHYWqMlEz'))
            payment = client.order.create({'amount':uamo,'currency':'INR','payment_capture':'1'})
            order = UserFunds(name = request.user,fd_owner=uname ,address=uadd ,email = uemail,amount = uamount,mobile=umob,order_id=payment['id'])
            order.save()
            context = {'form':form,'payment':payment,'name':uname,'address':uadd,'mobile':umob,'email':uemail}
            return render(request,'cust/applyfd.html',context) 
    else:
        form = UserFdDataForm()
    context = {'form':form}
    return render(request,'cust/applyfd.html',context) 


#  this function is for customer settings
def setting(request):
    return render(request,'cust/setting.html')


#  this function is for customer profile edit
def editprofile(request):
    user = request.user.userprofile
    form1 = profileform()
    if request.method == 'POST':
        form = UserEditform(instance=request.user ,data = request.POST)
        form1 = profileform( request.POST ,request.FILES ,instance=user )
        if form.is_valid():
            form.save()
        if form1.is_valid():
            form1.save()
    else:
        form = UserEditform(instance=request.user)
        form1 = profileform(instance=user)
    context = {'form':form ,'form1':form1}
    return render(request,'cust/editprofile.html',context)

# contact to support function
def contactus(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        text = request.POST.get('text')
        send_mail(
            # subject
            'testing',
            # msg
            'text',
            # from email
            settings.EMAIL_HOST_USER,
            # TO
            [email]

        )
    return render(request,'cust/contactus.html')

# about us function 
def aboutus(request):
    return render(request,'cust/aboutus.html')

def allforms(request):
    form = UserFunds.objects.all()
    context = {'form':form}
    return render(request,'cust/allforms.html',context)

# raz will send you post request
@csrf_exempt
def handelrequest(request):
    if request.method == 'POST':
        data = request.POST
        order_id = ""
        for key, value in data.items():
            if key == 'razorpay_order_id':
                order_id = value
                break
        status = UserFunds.objects.filter(order_id=order_id).first()
        status.payment_status = True
        status.certificate_status = 'Pending'
        status.save()
        msg_plane = render_to_string('cust/email.txt')
        msg_html = render_to_string('cust/email.html')
        send_mail(
            # subject
            'texting',
            # msg
            msg_plane,
            # settings
            settings.EMAIL_HOST_USER,
            # to
            [request.user.email],
            # html template
            html_message=msg_html
        )
    return HttpResponse('done')

# shows all fd that user have filled 
def userfdform(request):
    data = UserFunds.objects.filter(name__username = request.user.username)
    context = {'data':data}
    return render(request,'cust/userfdform.html',context)
    