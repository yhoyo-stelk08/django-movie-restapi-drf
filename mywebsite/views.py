from django.shortcuts import render

def index(request): 
    ctx = {
        'title' : 'Home Page'
    }
    return render(request,'index.html',ctx) 