from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide'),
]