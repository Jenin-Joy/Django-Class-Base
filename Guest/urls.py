from django.urls import path
from Guest import views
app_name = 'Guest'

urlpatterns = [
    path('shop/',views.Shop.as_view(),name="shop"),
]