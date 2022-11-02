from django.contrib import admin
from . import views
from teste import views
from teste.views import AnimaisListView, homeView
from teste.views import funcView
from django.urls import include, path, URLPattern


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path ('login/', funcView.as_view( template_name ='Login.html') ),
    path ('cadastro/', funcView.as_view( template_name ='cadastro.html') ),
    path('animais/', AnimaisListView.as_view(template_name='lista.hmtl') ),
    path ('animcad/', views.cad_animal, name = 'cad_animal'),
#    path ('animcad/', AnimaisListView.as_view( template_name ='Animcad.html') ),
    path ('home/', homeView.as_view( template_name ='home.html') ),

]