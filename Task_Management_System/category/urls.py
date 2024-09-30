
from django.urls import path
from .import views
urlpatterns = [
    path('category/',views.Mycategory,name='Mycategory'),
    
]
