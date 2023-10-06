from django.http import FileResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from api.models import Recomendacion

from frontend.forms import RecomendacionForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm 
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # usuario
                login(request, user)
                return redirect('login')
            except:
                # return HttpResponse('el usuario ya existe')
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error' : 'usario ya existe' 
                })
        # return HttpResponse('passwords no coinciden')
        return render(request, 'signup.html', {
            'form': UserCreationForm, 
            'error': 'passwords no coinciden'
    })


def startsession(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
        password=request.POST['password'])

        if user is None:
                return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'username or password incorrect'
            })
        else:
            login(request, user)
            return redirect('bandeja')
        

@login_required
def endsession(request):
    logout(request)
    return redirect('index')


def bandeja(request):
    recomendaciones = Recomendacion.objects.all()
    return render(request, 'recomendaciones.html', {
        'recomendaciones': recomendaciones
    })


def crear_reco(request):
    if request.method == 'POST':
        form = RecomendacionForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('bandeja')   

    else:
        form = RecomendacionForm()
        return render(request, 'crear.html', {
        'form': form
    }) 


def detail(request, pk):
    recomendacion = get_object_or_404(Recomendacion, pk=pk)
    # print(pk)
    return render(request, 'detalle.html', {
        'recomendacion': recomendacion
    })


def obtener_pdf(request, pdf_id):
    pdf = get_object_or_404(Recomendacion, pk = pdf_id)
    response = FileResponse(pdf.archivo, content_type='application/pdf')
    return response