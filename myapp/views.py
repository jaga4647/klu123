from . forms import CustomerForm
from . models import Customer
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q



def forgotpassword(request):
  return render(request, "forgetpassword.html")


def login(request):
  return render(request, "login.html")

def index(request):
  return render(request, "index.html")

def bookcar1(request):
  return render(request, "bookcar1.html")

def bookcar2(request):
  return render(request, "bookcar2.html")

def bookcar3(request):
  return render(request, "bookcar3.html")

def bookcar4(request):
  return render(request, "bookcar4.html")

def bookcar5(request):
  return render(request, "bookcar5.html")

def bookcar6(request):
  return render(request, "bookcar6.html")

def bookcar7(request):
  return render(request, "bookcar7.html")

def bookcar8(request):
  return render(request, "bookcar8.html")

def bookcar9(request):
  return render(request, "bookcar9.html")

def bookcar10(request):
  return render(request, "bookcar10.html")

def usedbookcar1(request):
  return render(request, "usedbookcar1.html")

def usedbookcar2(request):
  return render(request, "usedbookcar2.html")

def usedbookcar3(request):
  return render(request, "usedbookcar3.html")

def usedbookcar4(request):
  return render(request, "usedbookcar4.html")

def usedbookcar5(request):
  return render(request, "usedbookcar5.html")

def usedbookcar6(request):
  return render(request, "usedbookcar6.html")

def usedbookcar7(request):
  return render(request, "usedbookcar7.html")

def usedbookcar8(request):
  return render(request, "usedbookcar8.html")

def usedbookcar9(request):
  return render(request, "usedbookcar9.html")

def usedbookcar10(request):
  return render(request, "usedbookcar10.html")

def newVersion_usertable(request):
  return render(request, "newVersion_usertable.html")

def signUpForm(request):
  return render(request, "signupForm.html")

def adminlogin(request):
  return render(request, "adminlogin.html")


def contact_us(request):
  return render(request, "contact_us.html")



def adminvehicles(request):
  return render(request, "adminvehicles.html")





def adduser(request):
  if request.method =='POST':
    name = request.POST["name"]
    email = request.POST["email"]
    password = request.POST["pswd"]
    flag = Customer.objects.create(customer_name=name, personal_mail=email, password=password)
    if flag:
      return render(request, "login.html")
  else:
    return HttpResponse("Student Not Added")
  return HttpResponse("error")

def checklogin(request):
  if request.method == "POST":
    username = request.POST["email"]
    password = request.POST["pwd"]
    flag = Customer.objects.filter( Q(personal_mail=username) & Q(password=password) )
    if flag:
      return render(request ,"index.html")
    else:
      return HttpResponse("Invalid Login")
  else:
    return HttpResponse("error")