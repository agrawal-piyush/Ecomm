from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about/', views.about, name='Aboutus'),
    path('contact/', views.contact, name='Contactus'),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('Search/', views.Search, name='Search'),
    path('productview/', views.product, name='ProductView'),
    path('checkout/', views.checkout, name='checkout'),

]
