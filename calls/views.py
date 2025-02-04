from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




# Create your views here.
@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = "index.html"