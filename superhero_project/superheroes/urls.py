from django.urls import path
from superheroes import views

app_name = 'superheroes'
urlpatterns = [
    path('index/', views.index, name = 'index')
]