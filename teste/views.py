from django.views.generic import ListView
from django.shortcuts import render

from teste.models import Animal, func

class AnimaisView(ListView):
    model = Animal
    template_name = '.html'
    
class funcView(ListView):
    model = func
    template_name = 'Login.html'
    
# {% for publisher in object_list %}
#        <li>{{ publisher.name }}</li>
#    {% endfor %}