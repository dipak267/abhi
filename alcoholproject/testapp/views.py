from django.shortcuts import render
from testapp.models import Alcohol
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
class AlcoholListView(ListView):
    model = Alcohol
class AlcoholDetailView(DetailView):
    model = Alcohol
class AlcoholCreateView(CreateView):
    model = Alcohol
    fields = '__all__'
    success_url = reverse_lazy('home')
class AlcoholupdateView(UpdateView):
    model = Alcohol
    fields = '__all__'
    success_url = reverse_lazy('home')

class AlcoholDeleteView(DeleteView):
    model = Alcohol
    success_url = reverse_lazy('home')
