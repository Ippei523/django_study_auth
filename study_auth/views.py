from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password

class UsersView(APIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.create(
            email=request.data['email'],
            password=make_password(request.data['password'])
        )
        return Response({'id': user.id})

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return Response([{'id': user.id, 'email': user.email} for user in users])
