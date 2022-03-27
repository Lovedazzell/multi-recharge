from django.urls import path
from. import views
from django.conf.urls.static import static
from django.conf import settings


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
    path('applyFd/<int:pk>/',views.applyFd,name = 'applyFd'),
    path('editprofile/',views.editprofile,name = 'editprofile'),
    path('setting/',views.setting,name = 'setting'),
    path('allforms/',views.allforms,name = 'allforms'),
    path('contactus/',views.contactus,name = 'contactus'),
    path('aboutus/',views.aboutus,name = 'aboutus'),
    path('handelrequest/',views.handelrequest,name = 'handelrequest'),
    path('certificate/',views.Viewpdf.as_view(),name = 'generate_certificate'),
    path('userfdform/',views.userfdform,name = 'userfdform'),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
