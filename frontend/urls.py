from django.urls import path
from frontend import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/',     views.signup,           name='signup'),
    path('login/',      views.startsession,     name='login'),
    path('logout/',     views.endsession,       name="logout"),
    path('bandeja/',    views.bandeja,          name='bandeja'),
    path('crear/',      views.crear_reco,       name='crear'),
    path('bandeja/detalle/<int:pk>/', views.detail,         name='detail'),
    path('obtener_pdf/<int:pdf_id>/', views.obtener_pdf,    name='obtener_pdf'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)