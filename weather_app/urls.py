from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('city/<str:city>', views.ob_havo_malumotlari)

]