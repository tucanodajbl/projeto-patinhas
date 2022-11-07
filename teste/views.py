from django.views.generic import ListView, CreateView, TemplateView, DetailView, View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from teste.models import Animal, func
from django.http import Http404
from .forms import AnimalForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'lista'

    def get_queryset(self):
        return Animal.objects.all()

def cad_animal(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AnimalForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            aux = Animal()
            aux.Nome = form.cleaned_data['nome']
            aux.Raça = form.cleaned_data['raca']
            aux.Idade_Aproximada = form.cleaned_data['idade']
            aux.Cor_do_Pelo = form.cleaned_data['pelo']
            aux.Porte = form.cleaned_data['porte']
            aux.Observações = form.cleaned_data['obs']
            aux.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/teste/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AnimalForm()

    return render(request, 'animcad.html', {'form': form})

#def index(request):
#    lista = Animal.objects.all()
#    context = {'lista': lista}
#    return render(request, 'index.html', context)

class DetailView(DetailView):
    model = Animal
    template_name = 'detail.html'

#def detail(request, animal_id):
#    try:
#        animal = Animal.objects.get(pk=animal_id)
#    except Animal.DoesNotExist:
#        raise Http404("Animal não encontrado")
#    return render(request, 'detail.html', {'animal': animal})

def registerPage(request):
    tio = UserCreationForm()


    if request.method == 'POST':
        tio = UserCreationForm(request.POST)
        if tio.is_valid():
            tio.save()

    context = {'tio': tio}
    return render(request, 'register.html', context)

def animal(request):
    return render(request, 'lista.html')

class AnimaisListView(ListView):
    model = Animal
    template_name = 'lista.html'
    
class funcView(ListView):
    model = func
    template_name = 'login.html'

class homeView(TemplateView):
    template_name = 'home.html'

def logoutUser(request):
    logout(request)
    return redirect('home')

    
    
# {% for publisher in object_list %}
#        <li>{{ publisher.name }}</li>
#    {% endfor %}