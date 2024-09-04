# autenticacion/urls.py

from django.urls import path

from .views import MyTokenObtainPairView, register

# importamos la vista que se encarga de refrescar el token 
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', register, name='register'),

    # como es un endpoint de rest_framework_simplejwt, se accede en una ruta token/ apartado de la url
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
