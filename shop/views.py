from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse,  reverse_lazy
from django.db import IntegrityError
from .models import Stuff, Cart, CartItem
from django.contrib import messages
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

class CartListView(LoginRequiredMixin, ListView):
    model = CartItem
    template_name = 'cart_list.html'
    context_object_name = 'cart_items'
    login_url = 'login'

    def get_queryset(self):
        try:
            cart = Cart.objects.get(user=self.request.user)
            return cart.items.all()
        except Cart.DoesNotExist:
            Cart.objects.create(user=self.request.user)  
            return CartItem.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            cart = Cart.objects.get(user=self.request.user)
            context['total_amount'] = cart.total
        except Cart.DoesNotExist:
            context['total_amount'] = 0.00 
        return context

class CartDeleteView(LoginRequiredMixin, DeleteView):
	model = models.Stuff
	template_name = 'cart_delete.html'
	success_url = reverse_lazy('cart')
	login_url = 'login'

def cart_add(request, stuff_id):
	if request.method == 'POST':
	    try:
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
	    except Cart.DoesNotExist:
	        return CartItem.objects.none()

	    return redirect('cart')

def cart_item_delete(request, pk):
    try:
        cart_item = CartItem.objects.get(pk=pk, cart__user=request.user)
        cart_item.delete()
        cart = cart_item.cart
        cart.total = CartItem.objects.filter(cart=cart).aggregate(total=models.Sum(models.F('quantity') * models.F('stuff__price')))['total'] or 0.00
        cart.save()
        messages.success(request, "Товар успешно удален из корзины.")
        return redirect('cart')
    except CartItem.DoesNotExist:
        messages.warning(request, "Товар уже удален или не существует.")
        return redirect('cart')
    except Exception as e:
        messages.error(request, f"Ошибка при удалении товара: {str(e)}")
        return redirect('cart')

def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)