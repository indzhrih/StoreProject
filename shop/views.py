from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse,  reverse_lazy
from django.db import IntegrityError
from .models import Stuff, Cart, CartItem
from . import models

class StuffListView(LoginRequiredMixin, ListView):
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
    model = CartItem
    template_name = 'cart_list.html'
    context_object_name = 'cart_items'
    login_url = 'login'

    def get_queryset(self):
        cart = Cart.objects.get(user=self.request.user)
        return cart.items.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.get(user=self.request.user)
        context['total_amount'] = cart.total
        return context

def cart_add(request, stuff_id):
    if request.method == 'POST':
        item = get_object_or_404(Stuff, pk=stuff_id)
        quantity = int(request.POST.get('quantity', 1))

        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = cart.items.get_or_create(stuff=item)
        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity
        cart_item.save()

        cart.total = sum(item.total_price() for item in cart.items.all())
        cart.save()

        return redirect('cart')