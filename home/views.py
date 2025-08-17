from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import string  
# Create your views here.
from home.models import Contact,ImportantLink
def home(request):
    return render(request,'home/index.html')


    
# Storing the sets of punctuation in variable result  
punc = string.punctuation  
def contact(request):
    # return HttpResponse('contact')
    if request.method=="POST":
        print('post')
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        content = request.POST['content']
        print(name,email,content,number)
        if len(name) >1 and len(name) < 30:
            pass
        else:
            messages.error(request,'length of Name should be greater than 2 and less than 30')
            return render(request,'home/contact.html')

        if len(email) >1 and len(email) < 30:
            pass
        else:
            messages.error(request,'email is not correct try again!!')
            return render(request,'home/contact.html')
        print(len(number))
        if len(number) > 9 and len(number) < 13:
            pass
        else:
            messages.error(request,'number not correct try again!!')
            return render(request,'home/contact.html')
        ins = Contact(name=name,email=email,content=content,number=number)
        ins.save()
        messages.success(request,'Thank You for contacting me!! Your message has been saved ')
        print('data has been saved to database')
    else:
        print('not post')
    return render(request,'home/contact.html')

def portfolio(request):
    all_links = ImportantLink.objects.all()
    links = {}
    for link in all_links:
        links[link.title] = link.url
    print(links)
    return render(request, 'home/portfolio.html', {"links": links,"allLinks" : all_links})

def worksample(request):
    # return HttpResponse('projects')
    return render(request,'home/worksample.html')

def projects(request):
    return render(request,'home/django.html')