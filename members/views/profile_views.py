from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from members.forms import studentForm
from members.models import Student
from django.contrib.auth.models import User
from members.decorator import *

@allowed_users(allowed_roles=['student'])
@login_required(login_url='login')
def profile_home(request):
    student = request.user.student
    form = studentForm(instance=student)
    context = {'form' : form}

    if request.method == 'POST':
        form = studentForm(request.POST, request.FILES, instance=student)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('profile_view')

    return render(request, 'members/profile.html', context)

@allowed_users(allowed_roles=['student'])
@login_required(login_url='login')
def profile_view(request):
    student = request.user.student
    context={'stu' : student}
    return render(request, 'members/profile_view.html', context)

@allowed_users(allowed_roles=['student'])
@login_required(login_url='login')
def view_and_update_profile(request):
    return render(request,'members/profile_view_and_update.html')