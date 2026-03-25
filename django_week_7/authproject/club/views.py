from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView

def home_view(request):
    return HttpResponse("<h1>Welcome to the Club Lobby.</h1>")

class MemberView(LoginRequiredMixin, TemplateView):
    template_name = 'memberView.html'

class ManagerOffice(PermissionRequiredMixin, TemplateView):
    template_name = 'office.html'
    permission_required = 'club.can_view_office'
    raise_exception = True
    
    