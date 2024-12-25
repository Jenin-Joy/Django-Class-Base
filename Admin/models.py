from django.db import models

# Create your models here.

class District(models.Model):
    district_name = models.CharField(max_length=30)

    def __str__(self):
        return self.district_name

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

class Place(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=30)

    def __str__(self):
        return self.place_name

class Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory_name