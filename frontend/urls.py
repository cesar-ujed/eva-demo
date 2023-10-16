from django.urls import path
from frontend import views
from django.conf import settings
from django.conf.urls.static import static
from .views import BusquedaView

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/',     views.signup,           name='signup'),
    path('login/',      views.startsession,     name='login'),
    path('logout/',     views.endsession,       name="logout"),
    # path('bandeja/',    views.bandeja,          name='bandeja'),
    path('crear/',      views.crear_reco,       name='crear'),
    path('bandeja/detalle/<int:pk>/', views.detail,         name='detail'),
    path('obtener_pdf/<int:pdf_id>/', views.obtener_pdf,    name='obtener_pdf'),
    path('buscar/',     BusquedaView.as_view(), name='buscar'),
    path('salir/', views.salirView, name='salir'),
    path('bandeja/detalle/<int:pk>/actualizar/', views.actualizar, name='observacion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)