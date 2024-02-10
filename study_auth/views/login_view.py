from ..models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import check_password


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        password = request.data["password"]
        user = User.objects.get(
            email=email,
        )
        if user is None:
            return Response({"message": "ユーザーが見つかりません"}, status=400)

        if not check_password(password, user.password):
            return Response({"message": "パスワードが正しくありません"}, status=400)

        refresh = RefreshToken.for_user(user)
        token = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response({"token": token})
