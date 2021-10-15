from .models import student
from django.shortcuts import render
import random
from datetime import date
from django.contrib import auth

# Create your views here.
def apply(request):
    if request.method=="GET":
        return render(request,'apply.html')
    name=request.POST.get('name')
    ftname=request.POST.get('ftname')
    gender=request.POST.get('gender')
    dob=request.POST.get('dob')
    mob=request.POST.get('mob')
    email=request.POST.get('email')
    address=request.POST.get('address')
    pincode=request.POST.get('pincode')
    edu=request.POST.get('edu')
    college_name=request.POST.get('college_name')#check
    board=request.POST.get('board')
    percentage=request.POST.get('percentage')
    pic=request.POST.get('pfile')
    sign=request.POST.get('sfile')
    applieddate=date.today().strftime("%d/%m/%Y")
    application_id=random.randint(1000000000,9999999999)
    approve_status="pending"
    user=student.objects.create(application_id=application_id,name=name,ftname=ftname,gender=gender,dob=dob,mob=mob,email=email,address=address,pincode=pincode,edu=edu,college_name=college_name,board=board,percentage=percentage,pic=pic,sign=sign,applieddate=applieddate,approve_status=approve_status)
    user.save()
    return render(request,'home.html')

def show(request):
    user=student.objects.get(application_id='8467696021')
    print(user.name)
    return render(request,'udata.html',{'data' : user})

def login(request):
    if request.method=="GET":
        return render(request,'login.html')

def college(request):
    if request.method == "GET":
        return render(request,'login.html')
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=auth.authenticate(username=username,password=password)
    print(user)
    if user==None:
        return render(request,'login.html')
    show=student.objects.all();
    return render(request,'college.html',{'data': show})
    
    