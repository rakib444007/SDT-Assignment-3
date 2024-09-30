
from django.urls import path
from .import views
urlpatterns = [
    path('',views.Mytask,name='Mytask' ),
    path('show-task/',views.show_task,name='show_task'),
    path('edit-task/<int:id>',views.edit_task,name='edit_task'),
    path('show-task/<int:id>',views.delete_task,name='delete_task'),
   
]
