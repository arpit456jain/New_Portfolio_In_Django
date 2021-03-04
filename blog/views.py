from django.shortcuts import render,redirect
from blog.models import Contact
from django.contrib import  messages
from blog.models import Post
from django.contrib.auth.models import User 
# Create your views here.
from django.shortcuts import render, HttpResponse
from django.contrib.auth  import authenticate,  login, logout
import math
from blog.models import Post,BlogComment
from django.contrib import messages
# Create your views here.
from blog.templatetags import extra

# Create your views here.
def home(request): 
    
    allPosts = Post.objects.all()
    params = {}
    params['no_of_posts'] = 2
    last = math.ceil( len(allPosts) / int(params['no_of_posts']  ))
    print(len(allPosts),last,params['no_of_posts'])
    #logic for pagination for post in index.html
    page = request.GET.get('number')
    if not(str(page).isnumeric()):
        page = 1
    else:
        page = int(page)
        
    print("all goog till now",page)
    if len(allPosts)<params['no_of_posts']:
        print("test")
        prev = "#"
        next = "#"
    elif page == 1:
        prev = "#"
        next = "?number=" + str(int(page)+1)
    elif page == last:
        next = "#"
        prev = "?number=" + str(int(page)-1)
    else:
        prev = "?number=" + str(int(page)-1)
        next = "?number=" + str(int(page)+1)
    page=page-1
    allPosts = allPosts[page*int(params['no_of_posts']):page*int(params['no_of_posts'])+int(params['no_of_posts'])]
    params['allPosts']=allPosts
    params['prev'] = prev
    params['next'] = next
    return render(request,'myblog/home/home.html',params)

def contact(request):
    # return HttpResponse("This is contact")
    if request.method=="POST":
        print('post')
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    else:
        print('not post')
    return render(request,'myblog/home/contact.html')


def about(request): 
    # return HttpResponse('This is about')
    return render(request,'myblog/home/about.html')

def search(request):
    query=request.GET['query']
    # allPosts= Post.objects.filter(title__icontains=query)
    # allPosts= Post.objects.filter(content__icontains=query)
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts}
    # print(params)
    return render(request, 'myblog/home/search.html', params)
    
    
def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        exist = User.objects.all().filter(email=email)
        print(exist)
        if len(exist)!=0:
            messages.error(request, " email  already exist")
            return redirect('/myblog/')

        # check for errorneous input
         # check for errorneous input
        if len(username)<3:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/myblog/')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/myblog/')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
          # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('/myblog/')
                  

    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method=="POST":
        print('post')
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            print('loged in')
            return redirect("/myblog/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/myblog/")
    else:
        print('not post')
    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/myblog/')

def blogPost(request, slug): 
    # return HttpResponse(f'This is blogPost : {slug}')
    post = Post.objects.filter(slug=slug).first()
    post.views= post.views +1
    post.save()
    # yaha muje sirf vo 1st post chaiye as a object jiska slug mai bejumga bloghome se continue reading pe
    # print(post)
    comments= BlogComment.objects.filter(post=post,parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    print(replyDict)
    context={'post':post, 'comments': comments, 'user': request.user,'replyDict':replyDict}
    # context={"post":post}
    return render(request,'/myblog/home/blogPost.html',context)

def postComment(request):
    if request.method == "POST":
        print('in comment')
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/myblog/{post.slug}")
    # return redirect("/")