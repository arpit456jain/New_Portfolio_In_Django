from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

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
