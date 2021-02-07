from django.urls import path,include
from . import views 


urlpatterns = [
    path("",views.home,name="index"),
    path("topic",views.topic,name="topic"),
    
    path("country/<str:name>",views.countrySpecific,name="country"),
    path("country/<str:name>/<str:category>",views.countryCategory,name="countryCategory")
    
]