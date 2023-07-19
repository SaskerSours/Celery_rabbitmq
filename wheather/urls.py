from django.urls import path
from .views import debug, check_weather

urlpatterns = [
    path('ref/', debug, name='debug'),
    path('email-weather/', check_weather, name='weather')
]
