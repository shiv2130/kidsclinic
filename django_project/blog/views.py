from django.shortcuts import render
from .models import Post
# Create your views here.



def index(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'blog/index.htm', context)

def about(request):
    return render(request, 'blog/about.htm', {'title':'About'})    