from django.shortcuts import render,redirect,HttpResponse
from forms import Userform,UserProfileform, Backyardform
from django.views.decorators.csrf import csrf_exempt
from django.template.context import RequestContext
from django.contrib.auth import authenticate,logout,login
from models import BackyardModel
import cloudinary
import cloudinary.uploader
import cloudinary.api
# Create your views here.

cloudinary.config(
  cloud_name = "dpa3uyrsg",
  api_key = "634438172597289",
  api_secret = "pKq2pXgl6U41Vmlbttpy-pOXplc"
)


def index(request):
    Backyards = BackyardModel.objects.all()
    return render(request, 'Rbhome/index.html', {'Backyards':Backyards})


def searchview(request, searchtext):
    if searchtext=="":
        Backyards = BackyardModel.objects.all()
        return render(request, 'Rbhome/index.html', {'Backyards':Backyards})
    else:
        Backyards = list()
        Backyards.extend(BackyardModel.objects.filter(zip__icontains = searchtext))
        Backyards.extend(BackyardModel.objects.filter(state__icontains = searchtext))
        Backyards.extend(BackyardModel.objects.filter(city__icontains = searchtext))
        return render(request, 'Rbhome/index.html', {'Backyards': Backyards})


@csrf_exempt
def logoutview(request):
    logout(request)
    return redirect(index)


@csrf_exempt
def loginview(request):
    context = RequestContext(request)
    if request.method == 'POST':
        UserName = request.POST['username']
        PassWord = request.POST['password']
        User = authenticate(username=UserName,password=PassWord)
        if User:
            login(request, User)
            return redirect(index)
        else:
            return redirect(signupview)
    return render(request, 'Rbhome/login.html', context)


@csrf_exempt
def signupview(request):
    context = RequestContext(request)
    if request.method == 'POST':
        UserForm = Userform(data=request.POST)
        UserProfileForm = UserProfileform(data=request.POST)
        if UserForm.is_valid() and UserProfileForm.is_valid():
            User = UserForm.save()
            User.set_password(User.password)
            User.save()

            #profile_url = cloudinary.uploader.upload(request.FILES['Profile-pic'])

            UserProfile = UserProfileForm.save(commit=False)
            UserProfile.user = User
            #UserProfile.image_url = profile_url['url']
            UserProfile.save()
            return redirect(loginview)
        else:
            print UserForm.errors, UserProfileForm.errors

    else:
        UserForm = Userform()
        UserProfileForm = UserProfileform()
        return render(request,'Rbhome/signup.html', {'UserForm': UserForm, 'UserProfileForm': UserProfileForm},context)


@csrf_exempt
def proposalview(request):
    context = RequestContext(request)
    if request.method == 'POST':
        BackyardForm = Backyardform(data=request.POST)
        if BackyardForm.is_valid():
            Backyard = BackyardForm.save(commit=False)
            Backyard.user = request.user
            if 'Backyard1' in request.FILES:
                image_url1 = cloudinary.uploader.upload(request.FILES['Backyard1'])
                Backyard.image_url1 = image_url1['url']

            if 'Backyard2' in request.FILES:
                image_url2 = cloudinary.uploader.upload(request.FILES['Backyard2'])
                Backyard.image_url2 = image_url2['url']

            if 'Backyard3' in request.FILES:
                image_url3 = cloudinary.uploader.upload(request.FILES['Backyard3'])
                Backyard.image_url3 = image_url3['url']

            if 'Backyard4' in request.FILES:
                image_url4 = cloudinary.uploader.upload(request.FILES['Backyard4'])
                Backyard.image_url4 = image_url4['url']

            if 'Backyard5' in request.FILES:
                image_url5 = cloudinary.uploader.upload(request.FILES['Backyard5'])
                Backyard.image_url5 = image_url5['url']

            Backyard.save()
            return redirect(index)
        else:
            print BackyardForm.errors
    else:
        BackyardForm = Backyardform()
        return render(request,'Rbhome/proposal.html', {'BackyardForm': BackyardForm})