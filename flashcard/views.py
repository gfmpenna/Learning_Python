from django.shortcuts import render, redirect
from django.contrib.auth.models import User ,auth
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.

def novo_flashcard(request):
  
  if not request.user.is_authenticated:
    return redirect('/usuarios/login')
  
  if request.method == 'GET':
    return render(request,'novo_flashcard.html')
  
    
  '''return redirect('/usuarios/cadastro') '''