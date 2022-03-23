from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.
def index(request):
    blog=Blog.objects.all()
    
    return render(request,'index.html',{'blog':blog})
def posts(request,pk):
    post= get_object_or_404(Blog,id=pk)
    return render(request,'posts.html',{'post':post})