from django.contrib.auth.backends import ModelBackend
from .models import CustomUser


class IPAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # First authenticate with username/password via the parent class
        user = super().authenticate(request, username, password, **kwargs)

        # If credentials are valid, check the IP
        if user is not None and request is not None:
            client_ip = request.META.get('REMOTE_ADDR')

            # For proxy/load balancer environments (optional)
            # client_ip = request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0].strip() or request.META.get('REMOTE_ADDR')

            # Assuming your user model is CustomUser with allowed_ip field
            if user.allowed_ip and user.allowed_ip != client_ip:
                # IP doesn't match, authentication fails
                return None

        return user