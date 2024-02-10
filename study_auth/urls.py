from django.urls import path
from .views.register_views import RegisterView
from .views.login_view import LoginView

urlpatterns = [
    path("users/register/", RegisterView.as_view()),
    path("users/login/", LoginView.as_view()),
]
