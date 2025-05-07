from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Guest.models import *
from Admin.models import District
# Create your views here.

class Shop(CreateView):
    model = Shop
    fields = ['place', 'shop_name', 'shop_contact', 'shop_email', 'shop_address', 'shop_logo', 'shop_proof']
    success_url = reverse_lazy('shop_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['districts'] = District.objects.all()
        return context