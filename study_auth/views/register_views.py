from ..models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        if User.objects.filter(email=request.data['email']).exists():
            return Response({'message': 'メールアドレスはすでに存在しています'}, status=400)

        email = request.data['email']
        password = request.data['password']
        User.objects.create(
            email=email,
            password=make_password(password)
        )

        return Response({'message': 'Successfull registration'})
