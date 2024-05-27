from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'success': "Registration successful. Please login."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'register.html', {'error': error_message})

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,email = email ,password = password)
        if user is not None: #if there is user in database 
            login(request,user)
            return render("/dashboard")
        else:
            return render(request,'login.html',{'error': 'invalid user ,please try again'})
    
    return render(request,'login.html')

@login_required
def dashboard(request):
    
    return render(request,'dashboard.html')
