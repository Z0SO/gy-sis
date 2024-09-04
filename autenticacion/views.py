# from django.shortcuts import render

# tokenobtainpairview es una vista de django que se encarga de obtener el token de autenticación
# tokenrefreshview es una vista de django que se encarga de refrescar el token de autenticación
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# AllowAny es una clase de django que permite que cualquier usuario pueda acceder a la vista
from rest_framework.permissions import AllowAny

# User es una clase de django que representa un usuario
from django.contrib.auth.models import User

# status es una clase de django que contiene los códigos de estado de http
from rest_framework import status

# Response es una clase de django que permite devolver una respuesta http
from rest_framework.response import Response

# api_view es un decorador de django que permite definir una vista de django.
# permission_classes es un decorador de django que permite definir los permisos de una vista
from rest_framework.decorators import api_view, permission_classes

# RefreshToken es una clase de django que permite refrescar el token de autenticación
from rest_framework_simplejwt.tokens import RefreshToken


# para la parte del login, se crea una vista que hereda de TokenObtainPairView para que cualquier usuario pueda acceder a ella y obtener el token de autenticación

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)



# para el registro, se crea una vista que permite a cualquier usuario registrarse en la aplicación
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password)
    user.save()

    return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
