from django.shortcuts import render

from django.views.generic import ListView
from .models import Post

# Create your views here.
class HomePageView(ListView):
    # ListView returns an object called "object_list"
    # that we want to display in our template
    model = Post
    template_name = 'home.html'
    # context_object_name is used to clear the confusion by giving
    # a name to "object_list" like below line
    context_object_name = 'all_posts_list'
