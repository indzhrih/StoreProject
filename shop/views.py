from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from . import models

class HomePageView(TemplateView):
	template_name = 'home.html'

class StuffListView(ListView):
	model = models.Stuff
	template_name = 'stuff_list.html'

class StuffDetailView(DetailView):
	model = models.Stuff
	template_name = 'stuff_detail.html'
	success_url = reverse_lazy('stuff_list')

class StuffDeleteView(DeleteView):
	model = models.Stuff
	template_name = 'stuff_delete.html'
	success_url = reverse_lazy('stuff_list')

class StuffUpdateView(UpdateView):
	model = models.Stuff
	fields = ['title', 'body', 'price', 'image',]
	template_name = 'stuff_update.html'

class StuffCreateView(CreateView):
	model = models.Stuff
	fields = ['title', 'body', 'price', 'image',]
	template_name = 'stuff_create.html'