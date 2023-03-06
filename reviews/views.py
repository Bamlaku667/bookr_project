from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    name = "bamlaku"
    context = {
        'name': name
    }    
    return render(request, "base.html", context= context) #there are other options other than render 

def search(request):
    name = request.GET.get("search") or "<html/>"
    context = {'name': name}
    return render(request, "search.html", context= context)