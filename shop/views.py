from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse,  reverse_lazy
from . import models

class HomePageView(LoginRequiredMixin, TemplateView):
	template_name = 'home.html'

class StuffListView(ListView):
	model = models.Stuff
	template_name = 'stuff_list.html'
	login_url = 'login'


class StuffDetailView(LoginRequiredMixin, DetailView):
	model = models.Stuff
	template_name = 'stuff_detail.html'
	success_url = reverse_lazy('stuff_list')
	login_url = 'login'

class StuffDeleteView(LoginRequiredMixin, DeleteView):
	model = models.Stuff
	template_name = 'stuff_delete.html'
	success_url = reverse_lazy('stuff_list')
	login_url = 'login'

class StuffUpdateView(LoginRequiredMixin, UpdateView):
	model = models.Stuff
	fields = ['title', 'body', 'price', 'image',]
	template_name = 'stuff_update.html'
	login_url = 'login'

class StuffCreateView(LoginRequiredMixin, CreateView):
	model = models.Stuff
	fields = ['title', 'body', 'price', 'image',]
	template_name = 'stuff_create.html'
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class CartListView(ListView):
	model = models.Cart
	template_name = 'cart_list.html'

#def cart_add(request, stuff_id):
#	if request.method == 'POST':
#	    item = models.Stuff.objects.get(pk = stuff_id) 
#	    models.Cart.objects.create(stuff = item)
#	    success_url = reverse_lazy('cart_list')