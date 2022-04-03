from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('bookcar1/', views.bookcar1, name="bookcar1"),
    path('bookcar2/', views.bookcar2, name="bookcar2"),
    path('bookcar3/', views.bookcar3, name="bookcar3"),
    path('bookcar4/', views.bookcar4, name="bookcar4"),
    path('bookcar5/', views.bookcar5, name="bookcar5"),
    path('bookcar6/', views.bookcar6, name="bookcar6"),
    path('bookcar7/', views.bookcar7, name="bookcar7"),
    path('bookcar8/', views.bookcar8, name="bookcar8"),
    path('bookcar9/', views.bookcar9, name="bookcar9"),
    path('bookcar10/', views.bookcar10, name="bookcar10"),
    path('usedbookcar1/', views.usedbookcar1, name="usedbookcar1"),
    path('usedbookcar2/', views.usedbookcar2, name="usedbookcar2"),
    path('usedbookcar3/', views.usedbookcar3, name="usedbookcar3"),
    path('usedbookcar4/', views.usedbookcar4, name="usedbookcar4"),
    path('usedbookcar5/', views.usedbookcar5, name="usedbookcar5"),
    path('usedbookcar6/', views.usedbookcar6, name="usedbookcar6"),
    path('usedbookcar7/', views.usedbookcar7, name="usedbookcar7"),
    path('usedbookcar8/', views.usedbookcar8, name="usedbookcar8"),
    path('usedbookcar9/', views.usedbookcar9, name="usedbookcar9"),
    path('usedbookcar10/', views.usedbookcar10, name="usedbookcar10"),
    path('signUpForm/', views.signUpForm, name="signUpForm"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('adminvehicles/', views.adminvehicles, name="adminvehicles"),
    path('newVersion_usertable/', views.newVersion_usertable, name="newVersion_usertable"),
    path('forgotpassword/', views.forgotpassword,name="forgotpassword"),
]

