from django.shortcuts import render
from .models import Setting
# Create your views here.

def home(request):
    page='home'
    context = {'page':page}
    return render(request, 'home.html',context)

def contact(request):
    ct = Setting.objects.get(pk=1)
    context = {'ct':ct}
    return render(request,'contact.html',context)

def aboutUs(request):
    about = Setting.objects.get(pk=1)
    context = {'about':about}
    return render(request,'about_us.html',context)