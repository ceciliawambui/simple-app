from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')



def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


