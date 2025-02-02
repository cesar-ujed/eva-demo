import os
import zipfile
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views import View
from api.models import Recomendacion, Archivo
from frontend.forms import RecomendacionForm, BootstrapAuthenticationForm, ArchivoUpForm
from django.views.generic import ListView, DeleteView
from django.db.models import Q

# Create your views here.
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
                #login(request, user)
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


def index(request):
    if request.method == 'GET':
        # Cierra la sesión si el usuario está autenticado y vuelve a la página de login
        if request.user.is_authenticated:
            logout(request)
        
        return render(request, 'signin.html', {
            'form': BootstrapAuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': BootstrapAuthenticationForm,
                'error': 'Usuario o contraseña incorrecto'
            })
        else:
            login(request, user)
            return redirect('buscar')
        

@login_required
def endsession(request):
    logout(request)
    return redirect(index)


@login_required
def crear_reco(request):
    if request.method == 'POST':
        form = RecomendacionForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('buscar')   

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



class BusquedaView(ListView):
    model = Recomendacion
    template_name = 'search.html'
    context_object_name = 'resultados'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            # Asegúrate de apuntar a un campo específico de la relación ForeignKey
            return Recomendacion.objects.filter(
                Q(responsables__area_resp__icontains=query) |  # Cambia 'nombre' por el campo específico
                Q(categoria__eje__numero_eje__icontains=query)  # Cambia 'nombre' por el campo específico
            ).order_by('id')
        else:
            return Recomendacion.objects.all().order_by('id')

        

def salirView(request):
    return render(request, 'salirPage.html', {
        'msg': 'Estas seguro de salir?'
    })


def actualizar(request, pk):
    recomendacion = get_object_or_404(Recomendacion, pk=pk)
    #print(pk)

    if request.method == 'POST':
        observacion = request.POST.get('observacion')
        recomendacion.observacion = observacion
        recomendacion.save()
        return redirect('detail', pk)
    else:
        return render(request, 'observacion.html', {
            'recomendacion': recomendacion
        })
    

def up_archivo(request, pk):
    recomendacion = get_object_or_404(Recomendacion, pk=pk)

    if request.method == 'POST':
        form = ArchivoUpForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.save(commit=False)
            archivo.recomendacion = recomendacion  # Relaciona el archivo con la recomendación
            archivo.save()
            return redirect('detail', pk=pk)  # Redirige a la vista de detalle
    else:
        form = ArchivoUpForm()
    
    return render(request, 'evidencia.html', {'form': form, 'recomendacion': recomendacion})


def descargar_evidencias(request, recomendacion_pk):
    recomendacion = get_object_or_404(Recomendacion, pk=recomendacion_pk)
    evidencias = Archivo.objects.filter(recomendacion=recomendacion)

    # Crea el archivo ZIP en memoria
    response = HttpResponse(content_type='application/zip')
    zip_filename = f'evidencias_recomendacion_{recomendacion_pk}.zip'
    response['Content-Disposition'] = f'attachment; filename={zip_filename}'

    with zipfile.ZipFile(response, 'w') as zip_file:
        for evidencia in evidencias:
            evidencia_path = evidencia.archivo.path
            # Añade el archivo al ZIP
            zip_file.write(evidencia_path, os.path.basename(evidencia_path))

    return response


class RecomendacionDeleteView(DeleteView):
    model = Recomendacion
    template_name = 'eliminar_recomendacion.html'  # Plantilla de confirmación de eliminación
    success_url = reverse_lazy('buscar')  # Redirige después de la eliminación

    def get_object(self, queryset=None):
        """Método para obtener la recomendación que se eliminará."""
        obj = super().get_object(queryset=queryset)
        return obj    