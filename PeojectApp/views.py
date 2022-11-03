from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from PeojectApp.models import Desigination, VehicleRegistration, registration
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request,'home.html')

def base(request):
    return render(request,'base.html')

def load_signup(request):
    std=Desigination.objects.all()
    return render(request,'signup.html',{'std':std})


def add_registration(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']
        desiginations=request.POST['desiginations']
        
        if password == confirmpassword:
            if  User.objects.filter(username=username):
                messages.info(request,'username already exists')
                return redirect('add_registration')
            elif registration.objects.filter(username=username):
                messages.info(request,'username already exists')
                return redirect('add_registration')
                
            else:
                user = registration(first_name=firstname,last_name=lastname,email=email,username=username,password=password,
                                    desigination_id=desiginations)
                user.save()
                print('hi')
                msg_success = "Registration Successfull"
                messages.success(request, 'Profile Details Updated')
                return render(request,'signup.html',{'msg_success':msg_success})
        else:
            messages.info(request, 'password not matching')
            return redirect('add_registration')
   
    return redirect('load_signup')




def loginpage(request):
    return render(request,'login.html')


@login_required(login_url='loginpage')
def super_admin_welcome(request):
    return render(request,'super_admin.html')


def user_login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['usid']=user.id
            return redirect('super_admin') 
        
        elif registration.objects.filter(username=username,password=password,desigination_id=1):
            user1=registration.objects.get(username=username,password=password)
            request.session['usid']=user1.id
            
            return redirect('user_show_table')

        elif registration.objects.filter(username=username,password=password,desigination_id=2):
            user2=registration.objects.get(username=username,password=password)
            # auth.login(request,am)
            request.session['usid']=user2.id
           
            return redirect('admin_showtable')
        else:
            messages.error(request,'username does not exists')
    logout(request)    
    return render(request,'home.html')


    
@login_required(login_url='loginpage')
def admin_welcome(request):
    return render(request,'admin_welcome.html')
    

def super_admin(request):
    if 'usid' in request.session:
     
        return render(request,'super_admin.html')
    logout(request)
    return redirect('loginpage')  

@login_required(login_url='loginpage')
def vehicle_registration(request):
    return render(request,'vehicle_registration.html')

@login_required(login_url='loginpage')
def add_vehicle(request):
    if request.method=='POST':
        vnum=request.POST.get('vnum')
        vmodel=request.POST.get('vmodel')
        vtype=request.POST.get('vtype')
        vdes=request.POST.get('vdes')
        veh=VehicleRegistration(VehicleNumber=vnum,VehicleModel=vmodel,VehicleType=vtype,VehicleDescription=vdes,)
        veh.save()
        return redirect('add_vehicle')
    return render(request,'vehicle_registration.html')

@login_required(login_url='loginpage')
def super_admin_RegisteredVehicles(request):
    context=VehicleRegistration.objects.all()
    return render(request,'super_admin_RegisteredVehicles.html',{'dataread':context})



@login_required(login_url='loginpage')
def editpage(request,pk):
        reg=VehicleRegistration.objects.get(id=pk)

        return render(request,'editpage.html',{'reg':reg})



@login_required(login_url='loginpage')
def edit_details(request,pk):
    if request.method=='POST':
        reg1=VehicleRegistration.objects.get(id=pk)
        reg1.VehicleNumber=request.POST.get('vnum')
    
        reg1.VehicleModel=request.POST.get('vmodel')
        reg1.VehicleType=request.POST.get('vtype')
        
        reg1.VehicleDescription=request.POST.get('vdes')
       
        reg1.save()
        return redirect('super_admin_RegisteredVehicles')
    return render(request,'editpage.html')



@login_required(login_url='loginpage')
def delete(request,pk):
    st=VehicleRegistration.objects.get(id=pk)
    st.delete()
    return redirect('super_admin_RegisteredVehicles')

def admin_showtable(request):
    if 'usid' in request.session:
        context=VehicleRegistration.objects.all()
        return render(request,'admin_showtable.html',{'dataread1':context})
    logout(request)
    return redirect('loginpage') 



@login_required(login_url='loginpage')
def edit_details1(request,pk):
    if request.method=='POST':
        reg1=VehicleRegistration.objects.get(id=pk)
        reg1.VehicleNumber=request.POST.get('vnum')
    
        reg1.VehicleModel=request.POST.get('vmodel')
        reg1.VehicleType=request.POST.get('vtype')
        
        reg1.VehicleDescription=request.POST.get('vdes')
       
        reg1.save()
        return redirect('admin_showtable')
    return render(request,'editpage.html')



@login_required(login_url='loginpage')
def editpage1(request,pk):
        reg=VehicleRegistration.objects.get(id=pk)

        return render(request,'editpage.html',{'reg':reg})



@login_required(login_url='loginpage')
def designation(request):
    return render(request,'designation.html')



@login_required(login_url='loginpage')
def add_designation(request):
    if request.method=='POST':
        desigination=request.POST['des']
        crs=Desigination(desigination=desigination,)
        crs.save()
        print('hi')
        return redirect('add_designation')
    return render(request,'designation.html')



def user_show_table(request):
    if 'usid' in request.session:
        context=VehicleRegistration.objects.all()
        return render(request,'user_show_table.html',{'dataread2':context})

    logout(request)
    return redirect('loginpage')   

def user_logout(request):
    logout(request)
    return redirect('loginpage')



def edit4admin(request,pk):
    if 'usid' in request.session:

        reg=VehicleRegistration.objects.get(id=pk)
        return render(request,'edit4admin.html',{'reg':reg})
    logout(request)
    return redirect('loginpage') 
    


def edit_details2(request,pk):
    if 'usid' in request.session:

        if request.method=='POST':
            reg1=VehicleRegistration.objects.get(id=pk)
            reg1.VehicleNumber=request.POST.get('vnum')
        
            reg1.VehicleModel=request.POST.get('vmodel')
            reg1.VehicleType=request.POST.get('vtype')
            
            reg1.VehicleDescription=request.POST.get('vdes')
        
            reg1.save()
            return redirect('admin_showtable')
        return render(request,'edit4admin.html')
    logout(request)
    return redirect('loginpage') 

 
