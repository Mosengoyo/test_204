
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Panier
from .models import Product

def members(request):
	mymembers = Member.objects.all().values()
	template = loader.get_template('all_members.html')
	context = {
		'mymembers' : mymembers,
	}
	return HttpResponse(template.render(context, request))

def details(request, id):
	mymember = Member.objects.get(id=id)
	myproducts = Product.objects.get(id=id)
	template = loader.get_template('details.html')
	context = {
		'mymember' : mymember,
		'myproducts' : myproducts,
	}
	return HttpResponse(template.render(context, request))

def main(request):
	template = loader.get_template('PageAccueil/PageAc.html')
	return HttpResponse(template.render())

def ajouter_panier(request):
	myproduct = Product.objects.all().values()
	quantity = 1
	#total_price = quantity #*myproduct.price
	#panier_item = Panier(myproduct=myproduct, total_price=total_price, quantity=quantity)
	#panier_item.save()
	template = loader.get_template('PagePanier/all_products.html')
	context = {
		'myproduct' : myproduct,
	}
	return HttpResponse(template.render(context, request))  

def panier(request):
    panier_items = Panier.objects.filter(user=request.user)
    total_price = sum(item.total_price for item in panier_items)
    context = {'panier_items': panier_items, 'total_price': total_price}
    return render(request, 'PagePanier/Panier.html', context)

def checkout(request):
	template = loader.get_template('PageCheckout/Checkout.html')
	context = {}
	return HttpResponse(template.render())

def testing(request):
	template = loader.get_template('template.html')
	context = {
		'fruits': ['Apple', 'Banana', 'Cherry'],
	}
	return HttpResponse(template.render(context, request))