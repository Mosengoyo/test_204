
from django.shortcuts import render
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
	template = loader.get_template('details.html')
	context = {
		'mymember' : mymember,
	}
	return HttpResponse(template.render(context, request))

def main(request):
	template = loader.get_template('PageAccueil/PageAc.html')
	return HttpResponse(template.render())

def panier(request):
	#myproduct = Product.objects.get(id=id)
	template = loader.get_template('PagePanier/Panier.html')
	#context = {
#		'myproduct' : myproduct,#
#	}
	return HttpResponse(template.render()) # context, request

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