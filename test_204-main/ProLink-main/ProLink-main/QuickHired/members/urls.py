from django.urls import path
from . import views

urlpatterns = [
path('', views.main, name='main'),
path('panier/', views.panier, name = "panier"),
path('checkout/', views.checkout, name= "checkout"),
path('members/', views.members, name='members'),
path('products/', views.ajouter_panier, name='products'),
path('members/details/<int:id>', views.details, name='details'),
path('products/details/<int:id>', views.details, name='details'),
path('testing/', views.testing, name='testing'),
]
