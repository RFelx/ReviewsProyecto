from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Contenido, Review

def index(request):
    return render(request, 'reviewapp/index.html')

def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ya puedes iniciar sesión.')
            return redirect('login') 
    else:
        form = UserCreationForm()
    
    return render(request, 'reviewapp/registro.html', {'form': form})

def lista_contenido(request):
    contenidos = Contenido.objects.all()
    return render(request, 'reviewapp/contenido_list.html', {'contenidos': contenidos})

def contenido_detail(request, pk):

    contenido = get_object_or_404(Contenido, pk=pk)
    
    reviews = Review.objects.filter(contenido=contenido)

    if request.method == 'POST' and request.user.is_authenticated:
        argumento = request.POST.get('argumento')
        score = request.POST.get('score')
        
        if argumento and score:
            Review.objects.create(
                contenido=contenido,
                user=request.user,
                argumento=argumento,
                score=score
            )
            return redirect('detalle_contenido', pk=contenido.pk)

    return render(request, 'reviewapp/contenido_detail.html', {
        'contenido': contenido,
        'reviews': reviews
    })