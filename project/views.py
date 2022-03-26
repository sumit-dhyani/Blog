from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .forms import ArticleModelForm
from django.contrib.auth.models import User
# Create your views here.
# def index(request):
#     blog=Blog.objects.all()
class BlogListView(ListView):
    template_name='index.html'  
    queryset=Blog.objects.all()  
    # print(self.request.User)
#     return render(request,'index.html',{'blog':blog})
# def posts(request,pk):
#     post= get_object_or_404(Blog,id=pk)
#     return render(request,'posts.html',{'post':post})
class BlogDetailView(DetailView):
    template_name='posts.html'
    queryset=Blog.objects.all()

class BlogCreateView(CreateView):
    template_name='create.html'
    form_class=ArticleModelForm
    queryset=Blog.objects.all()
    success_url='/'
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
class BlogUpdateView(UpdateView):
    template_name='create.html'
    form_class=ArticleModelForm
    queryset=Blog.objects.all()
    success_url='/'
    # def get_object(self):
    #     id_=self.kwargs.get("pk")
    #     return get_object_or_404(Blog,id=id_)
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)