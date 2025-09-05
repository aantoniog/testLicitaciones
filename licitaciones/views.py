from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Licitacion

class LicitacionListView(ListView):
    model = Licitacion
    template_name = "lista.html"

class LicitacionCreateView(CreateView):
    model = Licitacion
    fields = "__all__"
    success_url = reverse_lazy("lista")
    template_name = "form.html"

class LicitacionUpdateView(UpdateView):
    model = Licitacion
    fields = "__all__"
    success_url = reverse_lazy("lista")
    template_name = "form.html"

class LicitacionDeleteView(DeleteView):
    model = Licitacion
    success_url = reverse_lazy("lista")
    template_name = "confirmar_borrar.html"
