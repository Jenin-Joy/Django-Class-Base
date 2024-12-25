from django.urls import path
from Admin import views
app_name = "Admin"
urlpatterns = [
    path('districtform/',views.DistrictView.as_view(),name="districtform"),
    path('districtlist/',views.DistrictList.as_view(),name="districtlist"),
    path('districtdeletelist/<pk>',views.Districtdeletelist.as_view(),name="districtdeletelist"),
    path('districteditlist/<pk>',views.Districteditlist.as_view(),name="districteditlist"),

    path('placeform/',views.PlaceView.as_view(),name="placeform"),
    path('placelist/',views.PlaceList.as_view(),name="placelist"),
    path('placedeletelist/<pk>',views.Placedeletelist.as_view(),name="placedeletelist"),
    path('placeeditlist/<pk>',views.Placeeditlist.as_view(),name="placeeditlist"),

    path('categoryform/',views.CategoryView.as_view(),name="categoryform"),
    path('categorylist/',views.CategoryList.as_view(),name="categorylist"),
    path('categorydeletelist/<pk>',views.Categorydeletelist.as_view(),name="categorydeletelist"),
    path('categoryeditlist/<pk>',views.Categoryeditlist.as_view(),name="categoryeditlist"),

    path('subcategoryview/',views.SubcategoryView.as_view(),name="subcategoryview"),
    path('subcategorylist/',views.SubcategoryList.as_view(),name="subcategorylist"),
    path('subcategorydeletelist/<pk>',views.Subcategorydeletelist.as_view(),name="subcategorydeletelist"),
    path('subcategoryeditlist/<pk>',views.Subcategoryeditlist.as_view(),name="subcategoryeditlist"),
]