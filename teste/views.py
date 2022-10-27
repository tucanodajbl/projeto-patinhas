from django.views.generic import ListView, CreateView
from django.shortcuts import render
from django.http import HttpResponse
from teste.models import Animal, func

def animal(request):
    return render(request, 'lista.html')

class AnimaisListView(ListView):
    model = Animal
    template_name = 'lista.html'
    
class funcView(ListView):
    model = func
    template_name = 'Login.html'
    
# {% for publisher in object_list %}
#        <li>{{ publisher.name }}</li>
#    {% endfor %}