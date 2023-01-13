from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('registration/', AddUser.as_view(), name='registration'),
]
