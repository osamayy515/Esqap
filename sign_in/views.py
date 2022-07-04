from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.
def sign_in(request):
    return render(request, 'sign-in.html', {})

def home(request):
    if request.method == "POST":
        user = UserForm(request.POST or None)
        if user.isvalid():
            user.save()
            return render(request, 'index.html', {})
    else:
        return render(request, 'index.html', {})
