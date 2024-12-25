from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Guest.models import *
# Create your views here.

class Shop(CreateView):
    model = Shop
    fields = ['shop_name', 'shop_contact', 'shop_email', 'shop_address', 'shop_logo', 'shop_proof']
    success_url = reverse_lazy('shop_list')