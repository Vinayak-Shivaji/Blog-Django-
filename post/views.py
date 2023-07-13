from django.shortcuts import render,redirect
from .models import post
from .forms import Form

# Create your views here.
def index(request):
    posts=post.objects.all()
    return render(request,'index.html',{'posts':posts})


def posts(request, pk):
    posts=post.objects.get(id=pk)
    return render(request,'posts.html',{'posts':posts})

def add(request):
    posts=post.objects.all()
    form=Form() 

    if request.method=='POST':
        form=Form(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
        
    context={'posts':posts,'form':form}       
    return render(request,'add.html',context)

