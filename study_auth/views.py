from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.create(email=email, password=password)
    return Response({'id': user.id, 'email': user.email, 'created_at': user.created_at, 'updated_at': user.updated_at,})
