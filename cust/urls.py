from django.urls import path
from. import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.profile,name='profile'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.userlogin,name='userlogin'),
    path('singup/',views.usersingup,name='usersingup'),
    path('logout/',views.userlogout,name='userlogout'),
    path('changepwd/',views.userpwdchange,name='userpwdchange'),
    path('adminuser/',views.admindisplay,name = 'admindisplay'),
    path('allusers/',views.allusers,name = 'allusers'),

    path('adminedit/<int:pk>/',views.admin_user_edit,name = 'admin_user_edit'),
    path('applyFd/',views.applyFd,name = 'applyFd'),


    path('editprofile/',views.editprofile,name = 'editprofile'),
    path('setting/',views.setting,name = 'setting'),
    path('allforms/',views.allforms,name = 'allforms'),
    path('contactus/',views.contactus,name = 'contactus'),
    path('aboutus/',views.aboutus,name = 'aboutus'),
    path('handelrequest/',views.handelrequest,name = 'handelrequest'),
    path('certificate/',views.Viewpdf.as_view(),name = 'generate_certificate'),
    path('userfdform/',views.userfdform,name = 'userfdform'),

    path('reset_password',auth_views.PasswordResetView.as_view(),name='reset_password'),

    path('reset_password_done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
