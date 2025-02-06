from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import LoginForm


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'signin.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('calls:home')



class CustomLogoutView(LogoutView):
    template_name = 'signin.html'

    # def dispatch(self, request, *args, **kwargs):
    #     messages.success(request, "You have been logged out successfully.")
    #     return super().dispatch(request, *args, **kwargs)


