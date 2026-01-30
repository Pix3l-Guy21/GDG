"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views as blogv
from blog.views import WelcomeView
from library import views as libv
from library.views import LoanView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', blogv.say_hello),
    path('posts/', blogv.get_all_posts),
    path('welcome/', WelcomeView.as_view()),
    path('books/', libv.get_all_books),
    path('loan/add/', LoanView.as_view())
]
