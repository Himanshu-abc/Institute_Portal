# from django.shortcuts import  render, redirect
# from members.forms import course_form,syllabus_form
# from members.models import *
#
# def add_Course(request):
#
#     form = course_form()
#     if request.method == 'POST':
#         form = course_form(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect('members_home')
#     context = {
#         'form':form
#     }
#     return render(request, 'members/add_course.html',context)
#
# def add_syllabus(request):
#
#     form = syllabus_form()
#     if request.method == 'POST':
#         form = syllabus_form(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect('members_home')
#     context = {
#         'form': form
#     }
#     return render(request, 'members/add_syllabus.html', context)
#
# def view_Course(request, name):
#
#     c = course.objects.get(name=name)
#     print(c)
#     context = {
#         'data':c
#     }
#     return render(request,'members/test.html',context)