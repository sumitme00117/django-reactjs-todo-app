from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-object/', views.get_object, name='get_object'),
    path('create-object/', views.create_object, name='create_object'),
    path('update-object/', views.update_object, name='update_object'),
    path('delete-object/', views.delete_object, name='delete_object'),

]