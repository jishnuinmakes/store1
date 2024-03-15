from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import DetailsForms
from django.http import JsonResponse
from .models import Course

# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,"password not matched")
            return redirect('register')

    return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def details(request):
    if request.method == 'POST':
        form = DetailsForms(request.POST)
        if form.is_valid():
            form.save()
            confirmation_message = "Order Confirmed"
            return render(request, 'details.html', {'confirmation_message': confirmation_message})
    else:
        form = DetailsForms()
    return render(request,'details.html',{'form':form})




def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id)
    course_list = [{'id': course.id, 'name': course.name} for course in courses]
    return JsonResponse(course_list, safe=False)

def success(request):
    return render(request, 'success.html')