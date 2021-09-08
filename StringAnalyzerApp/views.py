# i have created this -file Arpit Jain
from django.http import HttpResponse
from django.shortcuts import render,redirect
import string
from django.contrib import messages

def index(request):
    #3rd arg is a dict
    params = {'name':'arpit','age':'20'}
    return render(request,'string/index2.html',params)
    
def analyse(request):
    valueoftext = request.POST.get('text2', 'default')


    #check the values of checkboxes
    removepunc1 = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover= request.POST.get('newlineremover','off')
    extraspaceremover= request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    capitalize = request.POST.get('capitalize','off')

    purpose = ""
    # print(removepunc1,fullcaps,newlineremover,extraspaceremover)
    #value of punctuation
    result = string.punctuation
   # print(valueoftext,removepunc1,type(removepunc1),result ,type(result) )
    analysed_text = str(valueoftext)
    if removepunc1 == "on":
        #print('removepunc is on')
        analysed_text=''
        for char in valueoftext:
            if char not in result:
                analysed_text=analysed_text+char
        purpose = purpose + 'Removing punctuaions\n'
        params = {'purpose': purpose, 'analysed_text': analysed_text, 'valueoftext': removepunc1}
        valueoftext = analysed_text

    if capitalize == "on":
        analysed_text=valueoftext.capitalize()
        valueoftext = analysed_text
        #print("after uper" + analysed_text)
        purpose = purpose + 'capitalizing\n'
        params = {'purpose': purpose, 'analysed_text': analysed_text, 'valueoftext': capitalize}
    if fullcaps == "on":
        analysed_text=valueoftext.upper()
        valueoftext = analysed_text
        #print("after uper" + analysed_text)
        purpose = purpose + 'Coverting into upper-case\n'
        params = {'purpose': purpose, 'analysed_text': analysed_text, 'valueoftext': fullcaps}


    if newlineremover == "on":
            analysed_text = ""
            for char in valueoftext:
                if char == "\n" or char == "\r":
                    pass
                else:
                    analysed_text = analysed_text + char
            #print("pre", analysed_text)
            purpose = purpose + 'Removing new line\n'
            params = {'purpose': purpose, 'analysed_text': analysed_text, 'valueoftext':newlineremover}
            # print(params)
            valueoftext = analysed_text
    if extraspaceremover == "on":
                valueoftext = valueoftext.strip()
                # print('inside')
                analysed_text = ""
                try:

                    for  index,char in enumerate(valueoftext):
                        if valueoftext[index] == ' ' and valueoftext[index + 1] == ' ':
                            pass
                        else:
                            analysed_text=analysed_text+char
                except:
                    pass
                    # print('myerror ignore it',)
                finally:

                    # print("after extraspaceremover" + analysed_text)
                    valueoftext=analysed_text
                    purpose = purpose +  'Removing extra spaces\n'
                    params = {'purpose': purpose , 'analysed_text': analysed_text, 'valueoftext':extraspaceremover}
    if charcount == 'on':
        lenofstr = len(analysed_text)
        print(lenofstr,analysed_text,type(analysed_text))
        purpose = purpose + 'no of chars in output is ' + str(lenofstr) + "\n"
        params = {'purpose': purpose, 'analysed_text': analysed_text, 'valueoftext': charcount}

    if ((fullcaps == 'off' and removepunc1 == 'off') and (extraspaceremover == 'off' and newlineremover == 'off')) and charcount=='off':
        print('all checkbox is off')
        params = {'purpose': 'please select any operations', 'analysed_text': analysed_text, 'valueoftext':'off' }


    # return HttpResponse("<h1> analyse page</h1>")
    return render(request,'string/analyse.html',params)



