from django.contrib.auth.backends import ModelBackend
from users.models import CustomUser

class CustomAuthBackend(ModelBackend):
    def get_user(self, user_id):
        """Ensure Django retrieves the user from 'auth_db'"""
        try:
            return CustomUser.objects.using('auth_db').get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None