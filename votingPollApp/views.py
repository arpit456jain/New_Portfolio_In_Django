from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
global count_freq
count_freq = dict()
languages_for_checking = ['java','python','c++','c','php','perl',"kotlin","dart"]
languages = ['Java','Python','C++','C','Php','Perl',"Kotlin","Dart"]
def index(request):
    params = {'languages':languages}
    return render(request, 'votingPollApp/index.html',params)

def getQuery(request):
    q = request.GET['languages']
    q = q.lower()
    #using hashing we count freq of voting 
    if q in languages_for_checking:    
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


