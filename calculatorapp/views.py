from django.shortcuts import render
from django.http import HttpResponse
import smtplib #for email
from calculatorapp.models import UserFeedback

from django.contrib import messages
def connectTOMail():
    con = smtplib.SMTP("smtp.gmail.com",587)
    con.ehlo()
    # print("hello sucessfull")
    con.starttls()
    con.login("arpit456jain@gmail.com","#asdfghjkl#")
    print("login succesfull")
    return con

# Create your views here.
def index(request):
    
    return render(request,'calc/index2.html')

def calculate(request):
    if request.method == 'POST':
        print("post method")
        equation = request.POST['equation']
        # print(equation)
        # Exception Handling
        try:
            ans = eval(equation)
            final_msg = "Great!! your equation has been calculated {} = {}".format(equation, ans)
            messages.success(request, final_msg)
            
        except:
            messages.error(request,'Error Pattern of the equation is not correct Please check instructions first!!')
    
    return render(request,'calc/index2.html')

def feedback(request):
    if request.method == 'POST':
        try: 
            feedback = request.POST['feedback']
            name = request.POST['name']
            email = request.POST['email']

            # print(name,email,feedback)
            
            con = connectTOMail()
            con.sendmail("arpit456jain@gmail.com",email,"Subject:Feed Back of Calculator app \n\n"+"Thank You for the feed back")
            obj = UserFeedback(name=name,email=email,msg=feedback)
            obj.save()
            messages.success(request,'Thank You! Your feedback is very precious to us.')
        except Exception as e:
            messages.error(request,'Some Error occured '+str(e)+' please try again!')
    else:
        pass
        
    
    # return HttpResponse('feedback page')
    return render(request,'calc/feedback.html')