from django.shortcuts import render
from django.http import HttpResponse
import smtplib #for email
from votingPollApp.models import UserFeedback
from django.contrib import messages

# Create your views here.
global count_freq
count_freq = dict()
languages = ['Java','Python','C++','C','PHP']
def index(request):
    params = {'languages':languages}
    return render(request, 'votingPollApp/index.html',params)

def getQuery(request):
    q = request.GET['languages']
    #using hashing we count freq of voting 
    if q in languages:    
        if q in count_freq.keys():
            count_freq[q] +=1
        else:
            count_freq[q] = 1
        print(count_freq)
        params = {'languages':languages,'count_freq':count_freq,"error":False}
        messages.success(request, 'Succesfully added.')
    else:
        params = {'languages':languages,'count_freq':count_freq,"error":True}
        messages.error(request, 'this choice is not available please try again!!')
    return render(request, 'votingPollApp/index.html',params)


def connectTOMail():
    con = smtplib.SMTP("smtp.gmail.com",587)
    con.ehlo()
    print("hello sucessfull")
    con.starttls()
    con.login("arpit456jain@gmail.com","#vanshika jain#")
    print("login succesfull")
    return con



def feedback(request):
    if request.method == 'POST':
       
        feedback = request.POST['feedback']
        name = request.POST['name']
        email = request.POST['email']

        print(name,email,feedback)
        
        # con = connectTOMail()
        obj = UserFeedback(name=name,email=email,msg=feedback)
        obj.save()
        # con.sendmail("arpit456jain@gmail.com",email,"Subject:Feed Back of Calculator app \n\n"+"Thank You for the feed back")
        messages.success(request,"Thank You! Your feedback is very precious to us.")
    else:
        print("not post")
      
    # return HttpResponse('feedback page')
    return render(request,'votingPollApp/feedback.html')