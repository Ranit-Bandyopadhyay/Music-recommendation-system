from django.shortcuts import render
#from django.http import HttpResponse
#import music_recommendation

# Create your views here.
def home(request):
    return render(request,'recommendpg/home.html')

def login(request):
    return render(request,'recommendpg/login.html')
