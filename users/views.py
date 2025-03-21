from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect, request
from .forms import LoginForm


# Create your views here.



class CustomLoginView(LoginView):
    template_name = 'signin.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        """Check if user's IP matches the allowed_IP in their profile before login."""
        user = form.get_user()

        # Get client IP address
        client_ip = self.request.META.get('REMOTE_ADDR')

        # Authenticate using the custom backend
        user = authenticate(request=self.request, username=user.username, ip=client_ip)

        return super().form_valid(form)

        # if user is not None:
        #     login(self.request, user)
        #     return super().form_valid(form)
        # else:
        #     messages.error(self.request, _('Access denied. You can only login from your authorized IP address.'))
        #     return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        messages.error(self.request, _('Invalid username or password.'))
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('calls:home')


class CustomLogoutView(LogoutView):
    template_name = 'signin.html'

    # def dispatch(self, request, *args, **kwargs):
    #     messages.success(request, "You have been logged out successfully.")
    #     return super().dispatch(request, *args, **kwargs)


