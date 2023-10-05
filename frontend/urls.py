from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/',     views.signup,           name='signup'),
    path('login/',      views.startsession,     name='login'),
    path('logout/',     views.endsession,       name="logout"),
    path('bandeja/',    views.bandeja,          name='bandeja'),
]
