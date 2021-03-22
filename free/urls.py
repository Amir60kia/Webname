from django.urls import path
from . import views


app_name= 'free'
urlpatterns = [
    path('',views.free_list, name="list"),
    path('create',views.create_free,name="create"),
    path('<slug>',views.free_detial, name="detial"),
]
