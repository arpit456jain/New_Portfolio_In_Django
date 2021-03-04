from django.shortcuts import render,redirect
from django.http import HttpResponse
from ToDoListApp.models import Task
from django.contrib import messages

# Create your views here.
def home(request):
    # return HttpResponse('home')
    if request.method == 'POST':
        print('post')
        tastTitle  = request.POST['tastTitle']
        taskDesc = request.POST['taskDesc']
        print(tastTitle,taskDesc)
        if len(tastTitle)<2 or len(tastTitle)>30:
            messages.error(request,'length of title must not be greater than 30')
        else:
            newobj = Task(taskTitle=tastTitle,TaskDesc=taskDesc)
            newobj.save()
            messages.success(request,'Task Added Successfully!!')
    else:
        print('not pst')
    return render(request,'ToDoListApp/index.html')

def task(request):
    # return HttpResponse('home')
    alltasks = Task.objects.all()
    print(alltasks)
    params = {'alltasks':alltasks}
    return render(request,'ToDoListApp/task.html',params)

def search(request):
    if request.method=="GET":
        print('get')
        query = request.GET['query']
        t1 = Task.objects.filter(taskTitle__contains=query)
        t2 = Task.objects.filter(TaskDesc__contains=query)
        t3 = Task.objects.filter(TaskDesc__contains=query)
        t3 = t3.union(t1,t2)
        print(t3,type(t3))
        params = {'alltasks':t3}
        return render(request,'ToDoListApp/search.html',params)
    else:
        print('not get')
    return render(request,'ToDoListApp/search.html')


def deleteitem(request,slug):
    if request.method=="GET":
        print("get")
        slug=int(slug)
        print(slug,type(slug))
        # x = Task.objects.filter(id=id).delete()
        x = Task.objects.get(id = slug)  #
        print(x)
        try:
            x.delete()
            messages.success(request,'task is successfully deleted!')
            return redirect('/ToDoListApp/task/')
        except:
            messages.error(request,'Some error occured!!')
    else:
        print('not get')
    return HttpResponse('del')