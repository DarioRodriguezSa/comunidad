from django.urls import path
from . import views

app_name = "inicio"
urlpatterns = [

#---------------------ACTAS MATRIMONIALES------------------------    
    path('home/', views.home, name="activi"),


    

]