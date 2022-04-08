from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return HttpResponse("Polls index page")
s
def dataUpload(request):
    # To save data in Entry table in Linux
    a = 'queries1.csv'
    with open(a, 'r') as f:
        s = f.readlines()
        for i in s[1:]:
            l=i.split(',')
            qw = Entry.objects.filter(blog = l[0])
            if not qw:
                e = Entry()
                e.blog=Blog.objects.get(id=l[0])
                e.headline=l[1]
                e.body_text=l[2]
                e.pub_date=l[3]
                e.mod_date=l[4]      
                e.number_of_comments=l[5]
                e.number_of_pingbacks=l[6]
                e.rating=l[7][0]
                e.save()
            else:
                print("data is already there in db!!",l[0])      
                
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")
