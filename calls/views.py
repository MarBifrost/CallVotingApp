from django.http import Http404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from calls.models import Call


class HomeView(TemplateView):
    template_name = "index.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404("You have to be logged in.")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        call_date = today.strftime("%Y-%m-%d")

        # Get the total number of calls for today
        calls_count = Call.objects.filter(date=today).count()

        # Get the called_number from the GET request (if provided)
        called_number = self.request.GET.get('called_number')
        selected_date=self.request.GET.get('selected_date')
        start_date=self.request.GET.get('start_date')
        end_date=self.request.GET.get('end_date')

        called_number_count=None

        # If a called_number is provided, filter and count its occurrences
        if called_number:
            queryset=Call.objects.filter(called_number=called_number)

            if selected_date:
                queryset=queryset.filter(date=selected_date)

            if start_date and end_date:
                queryset=queryset.filter(date__range=[start_date,end_date])

            called_number_count=queryset.count()



        context['calls_count'] = calls_count
        context['called_number'] = called_number
        context['called_number_count'] = called_number_count
        context['selected_date'] = selected_date
        context['start_date'] = start_date
        context['end_date'] = end_date


        return context
