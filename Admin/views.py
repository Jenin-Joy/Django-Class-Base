from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from Admin.models import *
from django.urls import reverse_lazy
# Create your views here.

class DistrictView(CreateView):
    model = District
    fields = ['district_name']
    success_url = reverse_lazy('Admin:districtform')

class DistrictList(ListView):
    model = District

class Districtdeletelist(DeleteView):
    model = District
    success_url = reverse_lazy('Admin:districtlist')

class Districteditlist(UpdateView):
    model = District
    fields = ['district_name']
    success_url = reverse_lazy('Admin:districtlist')

class PlaceView(CreateView):
    model = Place
    fields = ['place_name', 'district']
    success_url = reverse_lazy('Admin:placeform')

class PlaceList(ListView):
    model = Place

class Placedeletelist(DeleteView):
    model = Place
    success_url = reverse_lazy('Admin:placelist')

class Placeeditlist(UpdateView):
    model = Place
    fields = ['place_name', 'district']
    success_url = reverse_lazy('Admin:placelist')

class CategoryView(CreateView):
    model = Category
    fields = ['category_name']
    success_url = reverse_lazy('Admin:categoryform')

class CategoryList(ListView):
    model = Category

class Categorydeletelist(DeleteView):
    model = Category
    success_url = reverse_lazy('Admin:categorylist')

class Categoryeditlist(UpdateView):
    model = Category
    fields = ['category_name']
    success_url = reverse_lazy('Admin:categorylist')

class SubcategoryView(CreateView):
    model = Subcategory
    fields = ['subcategory_name', 'category']
    success_url = reverse_lazy('Admin:subcategorylist')

class SubcategoryList(ListView):
    model = Subcategory

class Subcategorydeletelist(DeleteView):
    model = Subcategory
    success_url = reverse_lazy('Admin:subcategorylist')

class Subcategoryeditlist(UpdateView):
    model = Subcategory
    fields = ['subcategory_name', 'category']
    success_url = reverse_lazy('Admin:subcategorylist')