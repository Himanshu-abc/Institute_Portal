from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from members.models import *
from django.contrib import messages
from django.contrib.auth.models import Group, User
from members.forms import createuserForm
from members.decorator import *
from django.http import FileResponse

# Create your views here.

@admin_only
@login_required(login_url='login')
def home(request):
    context={}
    students = Student.objects.all()
    context['student']=students
    return render(request,'members/home.html',context,)

@login_required(login_url='login')
def members_home(request):

    News = News_gallery.objects.all().order_by('-id')[:3]

    Events = Upcoming_event.objects.all().order_by('-id')[:2]

    Images = Image_gallery.objects.all().order_by('-id')[:3]

    context = {'img': Images,'event': Events, 'news':News}
    return render(request,'members/members_dashboard.html',context,)

@unauthenticated_user
def registration(request):
    form = createuserForm()
    if request.method == 'POST':
        form = createuserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='student')
            user.groups.add(group)
            Student.objects.create(
                user = user,
            )
            messages.success(request, 'Account created for ' + username)
            return redirect('login')

    context = {'form' : form}
    return render(request,'members/student_register.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'members/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')

def deleteUser(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('home')
