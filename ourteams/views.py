from django.shortcuts import render,HttpResponse,redirect
from ourteams.models import OurGallery
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

auth_user = "root" #for adding members
params = {}
params['auth_user']=auth_user
def index(request):
    # return HttpResponse("hello")
    allmembers = OurGallery.objects.all()
    params['allmembers']=allmembers
    print(params)
    if request.method == 'POST':
        print('post')
        try:    
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone_number=request.POST.get('number')
            jobrole=request.POST.get('jobrole')
            fb_url=request.POST.get('fb_url')
            insta_url = request.POST.get('insta_url')
            github_url = request.POST.get('github_url')
            linkedn_url = request.POST.get('linkedn_url')
            img = None
            try:
                img=request.FILES['img']
            except:
                pass
            print(name, email, img,phone_number,jobrole,fb_url,insta_url,github_url,linkedn_url)
            entry = OurGallery(name=name, email=email, img=img,jobrole=jobrole,phone_number=phone_number,fb_url=fb_url,insta_url=insta_url,github_url=github_url,linkedn_url=linkedn_url)
            entry.save()
        except Exception as e:
            messages.error(request,"Some Error Occured"+ str(e))
    else:
        print('get')
    return render(request,'ourteams/ourteams.html',params)

def loginuser(request):
    if request.method == 'POST':
        print('post')
        try:
            uname = request.POST.get('uname')
            password = request.POST.get('password')
            user = authenticate(username=uname, password=password)
            print(user)
            if user is not None:
                print(user)
                login(request, user)
                messages.success(request,"Log in succesfullly")
                return redirect('/ourteams')
            else:
                messages.error(request,"Please Sign Up first")
                return redirect('/ourteams/signup')
        except Exception as e:
            messages.error(request,"Some Error Occured"+ str(e))
    else:
        print('get')
    # return HttpResponse("login")
    return render(request,'ourteams/login.html')
def signupuser(request):
    if request.method == 'POST':
        print('post')
        try:   
            uname = request.POST.get('uname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            if User.objects.filter(email=email).exists():
                messages.error(request,"Email already exists")
                return redirect('/ourteams/signup')
            # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
            user = User.objects.create_user(username=uname,email=email,password=password)
            user.save()
            messages.success(request,"User added succesfullly")
        except Exception as e:
            if str(e) == 'UNIQUE constraint failed: auth_user.username':
                print('yes')
                messages.error(request,"username already exists!!")
            else:
                print('no')
                messages.error(request,"Some Error Occured"+str(e))
    else:
        print('get')
    # return HttpResponse("signup")
    return render(request,'ourteams/signup.html')

def logoutuser(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please Login first")
        return redirect('/ourteams/login')
    else:    
        logout(request)
        messages.success(request,"Log out succesfullly")
        return redirect('/ourteams')

def edit(request,slug):
    print(slug)
    member = OurGallery.objects.filter(id=slug).first()
    params['member'] = member
    # print(member,type(member),member.id)
    if request.method == 'POST':
        try:
                
            print('post')
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone_number=request.POST.get('number')
            jobrole=request.POST.get('jobrole')
            fb_url=request.POST.get('fb_url')
            insta_url = request.POST.get('insta_url')
            github_url = request.POST.get('github_url')
            linkedn_url = request.POST.get('linkedn_url')
            img = None
            try:
                img=request.FILES['newimg']
            except:
                pass
            print(name, email,img)
            member.name=name
            member.email=email
            member.phone_number=phone_number
            member.jobrole=jobrole
            member.fb_url=fb_url
            member.insta_url=insta_url
            member.github_url=github_url
            member.linkedn_url=linkedn_url
            if img == None:
                pass
            else:
                member.img = img
            member.save()
            messages.success(request,"Edit Succesfully")
            return redirect('/ourteams')
        except Exception as e:
            messages.error(request, "Some Error Occured"+ str(e))
            return redirect('/ourteams/edit/'+str(slug))
    else:
        print('get')
    return render(request,'ourteams/edit.html',params)

def delete(request,slug):
    print(slug)
    try:
        member = OurGallery.objects.filter(id=slug)
        # print(member)
        member.delete()
        messages.success(request,"Member deleted")
    except Exception as e:
        messages.error(request,"Some Error Occured"+ str(e))
    return redirect('/ourteams')