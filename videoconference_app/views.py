from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


def index(request):
    return render(request, 'index.html')

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
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:#if user is in daatabase
            login(request, user)
            return redirect("/dashboard")
        else:
            return render(request, 'login.html', {'error': "Invalid credentials. Please try again."})

    return render(request, 'login.html')

@login_required
def dashboard(request):
    
    return render(request,'dashboard.html',{'name':request.user.username})

def JoinMeeting(request):
    if request.method == 'POST':
        roomID = request.POST['roomID'] 
        return redirect("/NewMeeting?roomID=" + roomID)
    return render(request, 'joinMeeting.html')

@login_required
def videoCall(request):
    return render(request,'video_call.html',{'name':request.user.username})

@login_required
def Logout_user(request):
    logout(request)
    return redirect('/login')



