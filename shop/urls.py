from django.urls import path
from . import views

urlpatterns = [
	path('', views.StuffListView.as_view(), name = 'stuff_list'),
	path('create/', views.StuffCreateView.as_view(), name = 'stuff_create'),
	path('<int:pk>/detail/', views.StuffDetailView.as_view(), name = 'stuff_detail'),
	path('<int:pk>/update/', views.StuffUpdateView.as_view(), name = 'stuff_update'),
	path('<int:pk>/delete/', views.StuffDeleteView.as_view(), name = 'stuff_delete'),
	path('add/<int:stuff_id>/', views.cart_add, name='cart_add'),
	path('cart/', views.CartListView.as_view(), name = 'cart'),
	path('cart/delete/<int:pk>/', views.cart_item_delete, name='cart_delete'),
]