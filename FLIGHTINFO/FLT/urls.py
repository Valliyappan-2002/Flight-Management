

from django.urls import path
from FLT import views


#Set the path to load appropriate functions for the request

urlpatterns = [
    path('SEARCHINFO/', views.searchInfo),
    path('UPDATEINFO/', views.updateInfo),
    path('SHOWINFO/', views.showInfo),
    path('UPDATEINFO/storeUpdate/<int:fn>', views.storeUpdate),
    ]
