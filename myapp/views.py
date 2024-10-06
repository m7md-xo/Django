from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

def hellow_world(request):
    return HttpResponse("Hello, World!")

from .models import BlogPost

def blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'myapp/blog_posts.html',{'posts':posts})

from django.shortcuts import render

def example_view(request):
    return render(request,'myapp/example.html')


from .forms import BlogPostForm

def add_blog_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_posts')
        else:
            form = BlogPostForm()
        return render(request,'add_post.html', {'form':form})