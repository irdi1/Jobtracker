from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSignupSerializer
from django.contrib.auth.models import User

# Create your views here.
class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]