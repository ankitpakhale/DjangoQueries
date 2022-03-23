from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
# Create your views here.

def signup(request):
    if request.POST:
        Name = request.POST['name']
        Email = request.POST['email']
        Number = request.POST['number']
        Address = request.POST['address']
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
            if len(Name) <= 0 or len(Email) <= 0 or len(Number) <= 0:
                messages.error(request, "Please fill the form correctly")
                
            elif (ConfirmPassword == Password) and (len(Number) == 10):
                v = userDetails(name = Name, email = Email, number = Number, address = Address, password = Password)
                v.save()    
                messages.success(request, 'Signup Successfully Done')
                # return render(request , 'login.html') 
                # return redirect('LOGIN')
            else:
                # msg = 'Please Enter Same Password'
                # return render(request , 'signup.html',{'msg':msg}) 
                messages.error(request, 'Please fill the form correctly')
        except(NameError):
            return render(request, '404-error-page.html')
        
        # except(TemplateDoesNotExist):
        #     return render(request, '404-error-page.html')

        # finally:
        #     messages.success(request, 'Signup Successfully Done...')
    return render(request,'signup.html')

def login(request):
    print('0')
    
    if request.method == 'POST':
        print("1")
        em = request.POST['email']
        pass1 = request.POST['password']
        try:
            print("2")
            if len(em) <= 0 or len(pass1) <= 0:
                print("3")
                messages.warning(request, 'Please fill all the given fields')
                # msg = "Please fill all the given fields" 
                # return render(request , 'login.html',{'msg':msg}) 
                return redirect('LOGIN')

            check = userDetails.objects.get(email = em)
            # nav bar HEADER NAME PENDING
            if check.password == pass1:
                print("4")
                request.session['email'] = check.email
                # nameMsg = userDetails.objects.all()
                messages.success(request, 'Logged in properly')
                return redirect('LOGIN')
                # return render(request,'home.html', {'key':nameMsg})
            else:
                print("5")
                messages.error(request, 'Invalid Password')
                return redirect('LOGIN')
                # msg = 'Invalid Password'
                # return render(request , 'login.html',{'msg':msg}) 
                # return render(request , 'wrongPassword.html',{'msg':msg}) 
            
        except(NameError):
            print("6")
            return render(request, '404-error-page.html')
       
        # except(TemplateDoesNotExist):
        #     return render(request, '404-error-page.html')
        
        except:
            print("7")
            msg = 'Invalid Email ID'
            # return render(request,'wrongPassword.html', {'msg':msg})
            messages.error(request, 'Invalid Email ID')
            return redirect('LOGIN')
    return render(request,'login.html')
