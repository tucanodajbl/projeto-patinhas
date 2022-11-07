from django.contrib import admin
from . import views
from teste import views
from teste.views import AnimaisListView, homeView, IndexView, DetailView, registerPage
from teste.views import funcView
from django.urls import include, path, URLPattern
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path ('register/', views.registerPage, name= 'registerPage'),
    path ('', login_required(IndexView.as_view( template_name='index.html'))),
    path('<int:pk>/', login_required(DetailView.as_view( template_name='detail.html'))),
    path ('login/', funcView.as_view( template_name ='Login.html') ),
#    path ('cadastro/', funcView.as_view( template_name ='cadastro.html') ),
#    path('animais/', AnimaisListView.as_view(template_name='lista.hmtl') ),
    path ('animcad/', login_required(views.cad_animal), name = 'cad_animal'),
#    path ('animcad/', AnimaisListView.as_view( template_name ='Animcad.html') ),
    path ('logout/', views.logoutUser, name = 'logoutUser')

]