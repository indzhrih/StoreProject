from django.urls import path
from . import views

urlpatterns = [
	path('', views.HomePageView.as_view(), name = 'home'),
	path('stuff/', views.StuffListView.as_view(), name = 'stuff_list'),
	path('stuff/create/', views.StuffCreateView.as_view(), name = 'stuff_create'),
	path('stuff/<int:pk>/detail/', views.StuffDetailView.as_view(), name = 'stuff_detail'),
	path('stuff/<int:pk>/update/', views.StuffUpdateView.as_view(), name = 'stuff_update'),
	path('stuff/<int:pk>/delete/', views.StuffDeleteView.as_view(), name = 'stuff_delete'),
	#path('cart/', views.CartListView.as_view(), name = 'cart_list'),
	#path('add_to_cart/<int:pk>/', views.cart_add, name = 'cart_add'),
]