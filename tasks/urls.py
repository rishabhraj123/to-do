from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('update_task/<int:id>/', views.updatetask, name='update'),
    path('delete_task/<int:id>/', views.deletetask, name='delete'),
    path('addheading/', views.addheading, name='addheading'),
    path('addtask/<int:id>/', views.addtask, name='addtask'),
]