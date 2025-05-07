from django.db import models
from Admin.models import Place
# Create your models here.

class Shop(models.Model):
    shop_name = models.CharField(max_length=30, help_text="Enter Shop Name")
    shop_contact = models.CharField(max_length=30, help_text="Enter Shop Contact")
    shop_email = models.EmailField(max_length=30, help_text="Enter Shop Email")
    shop_address = models.TextField(max_length=50, help_text="Enter Shop Address")
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    shop_logo = models.FileField(upload_to="Assets/Shop/Logo/")
    shop_proof = models.FileField(upload_to="Assets/Shop/Proof/")
    shop_password = models.CharField(max_length=30, help_text="Enter your password")

    def __str__(self):
        return self.shop_name