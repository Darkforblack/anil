from django.shortcuts import render,HttpResponse,redirect
from .models import NewUser,Course
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, logout
# Create your views here.

def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        re_password=request.POST['re_password']
        email=request.POST['email']
        if password==re_password :
            
            user=NewUser.objects.create_user(username=username,email=email,password=password)
            
            
           
        
            return redirect('login')
        
    return render(request,'register.html')


def handellogin(request):
    if request.method == 'POST':
        login_username = request.POST['login_username']
        login_password = request.POST['login_password']
        
        user =authenticate(username=login_username, password=login_password  )
        if user is not None and user.is_superuser==True:
            
            login(request, user)
            
            return redirect('dash')
        elif user is not None and user.is_staff==True and user.is_superuser==False and user.user_type=='teacher':
            
            login(request, user)
          
            return redirect('mainindex')
        elif user is not None and user.is_active==True and user.is_superuser==False  and user.is_staff==False:
            
            login(request, user)
            
      
            return redirect('mainindex2')
        
        elif user is not None and user.is_active==True and user.is_superuser==False  and user.is_staff==True and user.user_type=='receptionist':
            
            login(request, user)
            
         
            return redirect('rec_dash')
        
       
           
    
    return render(request, 'login.html')

def handellogout(request):
    logout(request)
   
    
    return redirect('index')

def mainindex(request):
    return render( request, "mainindex.html")

def mainindex2(request):
    return render( request, "mainindex2.html")


def profile(request):
    user = request.user


    return render(request, 'profile.html')

def pro_student(request):
    user = request.user
 

    return render(request, 'pro_student.html')
def dash(request):
  
    data2 = len(NewUser.objects.all().values().filter(user_type="student"))
    data3 = len(NewUser.objects.all().values().filter(user_type="teacher"))
    
    context={"data2":data2,"data3":data3}
    return render(request, 'dash.html', context)
def addcourse(request):
    if request.method=='POST':
        title=request.POST['title']
        description=request.POST['description']
        instructor=request.POST['instructor']
        fee=request.POST['fee']
        cour=Course(title=title,description=description,instructor=instructor,fee=fee)
        cour.save()
        return redirect('dash')
    
    # context={ }
    return render( request, "addcourse.html")

    
def allcourse(request):
    data =  Course.objects.all().values()
    return render(request, 'allcources.html', {'data': data})
    