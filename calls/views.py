from django.http import Http404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404("You have to be logged in.")
        return super(HomeView, self).dispatch(request, *args, **kwargs)