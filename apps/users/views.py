from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.contrib.auth.hashers import make_password

from .models import UserProfile

# Create your views here.	# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(
                Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
