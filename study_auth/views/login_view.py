from ..models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.get(
            email=email,
            password=password
        )
        if user is None:
            return Response({
                'message': 'メールアドレスまたはパスワードが間違っています'
            }, status=400)

        refresh = RefreshToken.for_user(user)
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response({'token': token})
