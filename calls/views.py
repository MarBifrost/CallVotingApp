from dbm import error
from django.http import Http404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from calls.models import CallsData



class HomeView(TemplateView):
    template_name = "index.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        print(f"User authenticated? {request.user.is_authenticated}")  # Debugging
        print(f"User: {request.user}")  # Debugging
        print(f"User database: {request.user._state.db}")  # Debugging

        if not request.user.is_authenticated:
            raise Http404("You have to be logged in.")

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        now_date = today.strftime("%Y-%m-%d")


        # Get the total number of calls for today
        calls_count = CallsData.objects.filter(call_date=today).count()


        # Get the called_number from the GET request (if provided)
        called_number = self.request.GET.get('called_number')
        only_called_number=self.request.GET.get('only_called_number')




        # selected_date=self.request.GET.get('selected_date')
        start_date=self.request.GET.get('start_date')
        end_date=self.request.GET.get('end_date')

        called_number_count=0
        only_date=0
        count_by_date=0
        error_message=""


        if self.request.GET:
            if called_number and start_date and end_date and called_number.isdigit():
                queryset=CallsData.objects.filter(call_date__range=(start_date,end_date), called_number=called_number)
                count_by_date=queryset.count()

            elif start_date and end_date:
                queryset=CallsData.objects.filter(call_date__range=(start_date,end_date))
                only_date=queryset.count()

            elif only_called_number and only_called_number.isdigit():
                queryset=CallsData.objects.filter(called_number=only_called_number)
                called_number_count=queryset.count()

            else:
                error_message="Please enter a valid data."




        context.update({
            'calls_count': calls_count,
            'called_number': called_number,
            'called_number_count': called_number_count,
            'start_date': start_date,
            'end_date': end_date,
            'count_by_date': count_by_date,
            'only_called_number': only_called_number,
            'now_date': now_date,
            'error_message': error_message,
            'only_date': only_date
        })


        return context
