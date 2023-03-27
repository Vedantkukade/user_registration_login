from django.shortcuts import render,redirect
# from .forms import registerform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import userregister
from datetime import datetime



# Create your views here.

def register(request):
    
    if request.method=='POST':
       user_name=request.POST.get('username')
       pass_word=request.POST.get('pass')
       f_name=request.POST.get('fname')
       l_name=request.POST.get('lname')
       d_ob=request.POST.get('dob')
       address_1=request.POST.get('address1')
       address_2=request.POST.get('address2')
       postalcode=request.POST.get('postal_code')
       phonenumber=request.POST.get('phone_number')

       new_user =User.objects.create_user(username=user_name,password=pass_word)
       new_user.first_name=f_name
       new_user.last_name=l_name
       data=userregister(username=user_name,fname=f_name,lname=l_name,dob=d_ob,address1=address_1,address2=address_2,postal_code=postalcode,phone_number=phonenumber)
       new_user.save()
       data.save()
       return redirect('userlogin')
    #     if rform.is_valid():
    #         rform.save
    #         return redirect('login')
    # else:
    #     rform=registerform()
    return render(request,'register.html',{})

def Login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['pass']

        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
    else:
        return render(request,"login.html")
    return render(request,"login.html")

@login_required
def home(request):
    current_time=datetime.now().time()
    data1=userregister.objects.filter(username=request.user)
    return render(request,'home.html',{'data2':data1,'curr':current_time})

def logoutuser(request):
    logout(request)
    return redirect('userlogin')

def indexpage(request):
    return render(request,'index.html')



