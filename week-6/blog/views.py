from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import View
# Create your views here.

def say_hello(request):
    return HttpResponse("Hello Blog")

def get_all_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        res = ", ".join([post.title for post in posts])
        return HttpResponse(f"All post titles: {res}")

class WelcomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to Django CBV")