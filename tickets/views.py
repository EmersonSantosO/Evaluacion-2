from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, DeleteView, UpdateView  
from django.views.generic.detail import DetailView
from .models import especialidadTI, soporteTI, tickets
from django.urls import reverse_lazy
from .forms import EspecialidadForm, SoporteForm, TicketsForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class TicketsList(ListView):
    model = tickets

method_decorator(staff_member_required, name='dispatch')
class EspecialidadCreate(CreateView):
    model = especialidadTI
    form_class = EspecialidadForm
    success_url = reverse_lazy('tickets_list')

class SoporteTICreate(CreateView):
    model=soporteTI
    form_class = SoporteForm
    success_url = reverse_lazy('tickets_list')

class TicketsCreate(CreateView):
    model=tickets
    form_class = TicketsForm
    success_url = reverse_lazy('tickets_list')

class TicketsUpdate(UpdateView):
    model = tickets
    form_class = TicketsForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('tickets_update_form', args=[self.object.id]) + '?ok'

method_decorator(staff_member_required, name='dispatch')
class TicketsDelete(DeleteView):
    model = tickets
    success_url = reverse_lazy('tickets_list')

class TicketsDetail(DetailView):
    model = tickets

def home(request):
    return render(request, 'tickets/home.html')
