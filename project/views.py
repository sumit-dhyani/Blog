from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import ArticleModelForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import BlogSerializer
from rest_framework import generics

class Blog_List(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
class Blog_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    def delete(self, request, *args, **kwargs):
        
        return super().delete(request, *args, **kwargs)
# def index(request):
#     blog=Blog.objects.all()
# @csrf_exempt
# @api_view(['GET', 'POST'])
# def Blog_List(request,format=None):
#     if request.method == 'GET':
#         snippets = Blog.objects.all()
#         serializer = BlogSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         # data = JSONParser().parse(request)
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def Blog_detail(request, pk,format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Blog.objects.get(pk=pk)
#     except Blog.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = BlogSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = BlogSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
class BlogListView(ListView):
    # paginate_by=4
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

class BlogDeleteView(DeleteView):
    template_name='delete.html'
    queryset=Blog.objects.all()
    success_url='/'