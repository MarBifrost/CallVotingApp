from django.urls import path
from .views import CustomLoginView, CustomLogoutView

app_name = 'users'

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
