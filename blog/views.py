from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic import DetailView
# Create your views here.
@login_required(login_url="/login")
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
