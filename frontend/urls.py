from django.urls import path
from frontend import views
from django.conf import settings
from django.conf.urls.static import static
from .views import BusquedaView

urlpatterns = [
    path('',                                    views.index,            name='index'),
    path('signup/',                             views.signup,           name='signup'),
    path('logout/',                             views.endsession,       name="logout"),
    path('crear/',                              views.crear_reco,       name='crear'),
    path('bandeja/detalle/<int:pk>/',           views.detail,           name='detail'),
    path('obtener_pdf/<int:pdf_id>/',           views.obtener_pdf,      name='obtener_pdf'),
    path('buscar/',                             BusquedaView.as_view(), name='buscar'),
    path('salir/',                              views.salirView,        name='salir'),
    path('bandeja/detalle/<int:pk>/actualizar/',views.actualizar,       name='observacion'),
    path('recomendacion/<int:pk>/subir_evidencia/',     views.up_archivo,           name='evidencia'),
    path('descargar-evidencias/<int:recomendacion_pk>/', views.descargar_evidencias, name='descargar_evidencias'),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)