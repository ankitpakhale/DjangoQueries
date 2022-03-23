from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
# Create your views here.

def signup(request):
    messages.error(request, 'Welcome to Signup')
    if request.POST:
        Name = request.POST['name']
        Email = request.POST['email']
        Number = request.POST['number']
        # Address = request.POST.get('address')
        Password = request.POST['password']
        ConfirmPassword = request.POST['confirmPassword']
        print(len(Password) + len(ConfirmPassword),'vsdvd')
        try:
            # if (len(Number) > 10) or (len(Number) < 10) :
            #     msg = "Phone number should be equal to 10 characters" 
            #     return render(request , 'signup.html',{'msg':msg}) 

            # elif (len(Password) < 8):
            #     msg = "Password should be greater than 8 characters" 
            #     return render(request , 'signup.html',{'msg':msg}) 
            
            if (ConfirmPassword == Password) or (Number == 10):
                v = userDetails()
                v.name = Name
                v.email = Email
                v.number = Number
                # v.address = Address
                v.password = Password
                v.confirmPassword = ConfirmPassword
                v.save()
                return redirect('LOGIN')
            else:
                msg = 'Please Enter Same Password'
                return render(request , 'signup.html',{'msg':msg}) 
        except(NameError):
            return render(request, '404-error-page.html')
        
        # except(TemplateDoesNotExist):
        #     return render(request, '404-error-page.html')

        finally:
            messages.success(request, 'Signup Successfully Done...')
    return render(request,'signup.html')

def login(request):
    if request.POST:
        em = request.POST.get('email')
        pass1 = request.POST.get('password')
        
        try:
            check = userDetails.objects.get(email = em)
            
            if (em == "" or pass1 == ""):
                msg = "Please fill all the given fields" 
                return render(request , 'login.html',{'msg':msg}) 
            
            # nav bar HEADER NAME PENDING
            elif check.password == pass1:
                request.session['email'] = check.email
                nameMsg = userDetails.objects.all()
                return HttpResponse("Logged in properly")
                # return redirect('HOME')
                # return render(request,'home.html', {'key':nameMsg})

            else:
                msg = 'Invalid Password'
                # return render(request , 'wrongPassword.html',{'msg':msg}) 
                return render(request , 'login.html',{'msg':msg}) 
            
        except(NameError):
            return render(request, '404-error-page.html')
       
        # except(TemplateDoesNotExist):
        #     return render(request, '404-error-page.html')
        
        except:
            msg = 'Invalid Email ID'
            # return render(request,'wrongPassword.html', {'msg':msg})
            return render(request,'login.html', {'msg':msg})

    return render(request,'login.html')
