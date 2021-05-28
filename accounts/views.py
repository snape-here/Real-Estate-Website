from django.contrib import messages
from django.shortcuts import redirect, render

# Create your views here.
def register(request):
    if request.method == 'POST':
        messages.error(request, 'ERROR MESSAGE')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'accounts/login.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return redirect('index')