# Message/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import Message

# Create your views here.

def index(request):
    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            Message.objects.create(message=message_content)
            return redirect('Message:index')  # Redirect ke halaman yang sama setelah menyimpan data
    return render(request, 'index.html')

def loginAdmin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        print(password)
        if user is not None and user.is_superuser:
            login(request, user)
            print("berhasil login")
            return redirect('Message:messageAdmin')  # Ganti dengan URL yang diinginkan setelah login
        else:
            # Jika login gagal, Anda bisa menambahkan pesan kesalahan di sini
            return render(request, 'login.html', {'error': 'Invalid email or password or not a superuser'})

    return render(request, 'login.html')

def messageAdmin(request):
    message = Message.objects.all().order_by('-message')
    return render(request, 'message.html', {'messages':message})
    
    