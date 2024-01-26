from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.messages import constants
from django.contrib import messages
from .models import Categoria, Flashcard

# Create your views here.


def novo_flashcard(request):
    if not request.user.is_authenticated:
        return redirect("/usuarios/login")
    if request.method == "GET":
        categorias = Categoria.objects.all()
        dificuldades = Flashcard.DIFICULDADE_CHOICES
        flashcard = Flashcard.objects.filter(user = request.user)
        
        categoria_filter = request.GET.get('categoria')
        dificuldade_filter = request.GET.get('dificuldade')
        
        if categoria_filter:
            flashcard = flashcard.filter(categoria__id = categoria_filter)
        
        if dificuldade_filter:
            flashcard = flashcard.filter(dificuldade = dificuldade_filter)
        
        return render(request, "novo_flashcard.html", {'categorias' : categorias, 'dificuldades' : dificuldades, 'flashcards' : flashcard})
    elif request.method == 'POST':
        pergunta = request.POST.get('pergunta')
        resposta = request.POST.get('resposta')
        categoria = request.POST.get('categoria')
        dificuldade = request.POST.get('dificuldade')
        
        if len(pergunta.strip()) == 0 or len(resposta.strip()) == 0:
            messages.add_message(request, constants.ERROR, "Preencha todos os Campos.")
            return redirect('/flashcard/novo_flashcard/')
        
        flashcard = Flashcard(
            user = request.user,
            pergunta = pergunta,
            resposta = resposta,
            categoria_id = categoria, #Aqui o Uso do _id, Indica que ele pegará o ID da categoria que está vindo diretamente do Method POST no request.
            dificuldade = dificuldade,
        )
        
        flashcard.save()
        messages.add_message(request, constants.SUCCESS, "FlashCard Cadastrado com Sucesso.")
        return redirect('/flashcard/novo_flashcard')