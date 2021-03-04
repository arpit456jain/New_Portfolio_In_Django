from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

# now for using login sys we import user model
from django.contrib.auth.models import User,auth

def signup(request):
    # return HttpResponse('signup')
    if request.method == "POST":
        # print('post')
        fname = request.POST['fname']
        sname = ""
        uname = request.POST['uname']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['cpassword']
         # validations
        if pass1 == pass2:
            # checking if username is exist
            if User.objects.filter(username=uname).exists():
                messages.error(request,'user already exist')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email already exist')
                else:
                    userobj = User.objects.create_user(username=uname,password=pass1,email = email,first_name=fname,last_name=sname)
                    userobj.save()
                    messages.success(request,'Successfully!! Registred')
                    # print('succesfully saved')
           
        else:
            messages.error(request,'password not matched')
        return redirect('/stringAnalyzer/')
    else:
        pass
        # print('not post')
    return render(request,'string/signup.html')

def login(request):
    # return HttpResponse('login')
    if request.method == 'POST':
        # print('post')
        username = request.POST['username']
        password = request.POST['password']
         #validating
        if username == "" or password == "":
            messages.error(request,'please fill all fields correctly!!')
        else:
            # now we will use auth for cheking existing user
            user = auth.authenticate(username=username,password=password)
            if user == None:
                # print('no acount')
                messages.error(request,'There is no account with this username Please Sign Up first!!')
                return redirect('/stringAnalyzer/registration/')
            else:
                # print('okay you can login')
                auth.login(request,user)
                messages.success(request,'Successfully Logged In!')
                return redirect('/stringAnalyzer/')
    else:
        pass
        # print('not post')
    return render(request,'string/login.html')

def logout(request):
    # return HttpResponse('logout')
    auth.logout(request)
    messages.success(request,'Succesfully Logged Out!!')
    return render(request,'string/index2.html')