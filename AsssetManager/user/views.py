from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import UserCreationForm
from django.views.generic  import CreateView,ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Register(LoginRequiredMixin,CreateView):
    model=User
    form_class=UserCreationForm
    template_name="user/registration.html"
    success_url="/asset/dashboard/"


def checkuser(request):
    username=request.POST.get("username")
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div style='color:green' id='username'> User Found</div>")
    else:
        return HttpResponse("<div style='color:red' id='username'>This Username is not found </div>")
    
def checkuser2(request):
    username=request.POST.get("username")
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div style='color:red' id='username'> A  user with this info exist</div>")
    else:
        return HttpResponse("<div style='color:green' id='username'>User name ok </div>")

def emailcheck(request):
    email=request.POST.get("email")
    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse("<div style='color:red' id='email'> A  user with this email exist</div>")
    else:
        return HttpResponse("<div style='color:green' id='email'>email is ok</div>")