from django.contrib import admin
from Admin.models import District,Category,Place
# Register your models here.

admin.site.register(District)
admin.site.register(Category)
admin.site.register(Place)
# admin.site.register(Shop)

# @admin.register(Shop)
# class ShopAdmin(admin.ModelAdmin):
#     list_display = (
#         'shop_name',
#         'shop_contact', 
#         'shop_email',
#         'shop_address',
#         'place',
#         'shop_logo',
#         'shop_proof'
#         )