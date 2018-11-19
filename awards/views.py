from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import categories,technologies,colors,countries,Project,Profile
from .forms import ProjectForm,ProfileForm
from decouple import config,Csv
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q

# Create your views here.
def index(request):
    date = dt.date.today()
    current_user = request.user
    profile =Profile.objects.get(username=current_user)

    winners=Project.objects.all()
    caraousel = Project.objects.get(id=8)

    return render(request,'index.html',{"winners":winners,"profile":profile,"caraousel":caraousel,"date":date})

def create_profile(request):
    current_user = request.user
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user

            profile.save()
    else:
        form=ProfileForm()

    return render(request,'create_profile.html',{"form":form})

def new_project(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.username = current_user
            project.avatar = profile.avatar
            project.country = profile.country

            project.save()
    else:
        form = ProjectForm()

    return render(request,'new_project.html',{"form":form})

def directory(request):
    date = dt.date.today()
    current_user = request.user
    profile =Profile.objects.get(username=current_user)

    winners=Project.objects.all()
    caraousel = Project.objects.get(id=8)

    return render(request,'directory.html',{"winners":winners,"profile":profile,"caraousel":caraousel,"date":date})

def profile(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    projects=Project.objects.filter(username=current_user)

    return render(request,'profile.html',{"projects":projects,"profile":profile})

def site(request,site_id):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)

    try:
        project = Project.objects.get(id=site_id)
    except:
        raise ObjectDoesNotExist()
    return render(request,"site.html",{"project":project,"profile":profile})
