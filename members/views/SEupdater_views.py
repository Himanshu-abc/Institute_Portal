from django.http import HttpRequest,HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from members.forms import Image_galleryForm
from members.models import Image_gallery,Upcoming_event,News_gallery
from members.forms import *
from django.forms import inlineformset_factory
from members.decorator import *
from django.http import FileResponse
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def addimagesG(request):

    form = Image_galleryForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form=Image_galleryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('members_home')

    return render(request, 'members/Image_gallery.html' ,context )

def update_Events(request):

    form = Event_updatesForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form=Event_updatesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members_home')

    return render(request, 'members/updateEvents.html' ,context )

def update_News(request):

    form = News_galleryForm()
    context = {
        'form':form
    }
    if request.method == 'POST':
        form=News_galleryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members_home')

    return render(request, 'members/updateNews.html' ,context )

@xframe_options_exempt
@xframe_options_sameorigin
def view_news(request):
    news = News_gallery.objects.all().order_by('-id')[:2]

    # url_list=[]
    # for i in news:
    #     url_list.append(i.news_pdf.url)

    context = {
        'data': news
    }
    return render(request,'members/test.html',context)

